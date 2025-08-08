import io

import pandas as pd
from pandas import DataFrame
from xlsxwriter import Workbook

from logic.cal_grafic import calculos_graficos


def _excel_letter_to_index(letter: str) -> int:
    """
    Convierte una letra(s) de Excel (p.ej. 'A', 'F', 'AA') a índice 0-based.
    A -> 0, B -> 1, ..., Z -> 25, AA -> 26, AB -> 27, etc.
    """
    s = letter.strip().upper()
    val = 0
    for ch in s:
        if not ("A" <= ch <= "Z"):
            raise ValueError(f"Letra de Excel inválida: {letter!r}")
        val = val * 26 + (ord(ch) - ord("A") + 1)
    return val - 1  # 0-based


def generar_excel(
    df_fil: DataFrame,
    min_peso: float,
    max_peso: float,
    min_ancho: float,
    max_ancho: float,
    min_largo: float,
    max_largo: float,
) -> bytes:
    """
    Genera un Excel con hoja 'datos' y una hoja 'grafico' con el chart.
    Aquí NO se pasan letras como parámetros externos; se definen al llamar a `graficos`.
    """
    output = io.BytesIO()

    with pd.ExcelWriter(
        output,
        engine="xlsxwriter",
        datetime_format="yyyy-mm-dd",
        date_format="yyyy-mm-dd",
    ) as writer:

        sheet_name = "datos"
        df_fil.to_excel(writer, index=False, sheet_name=sheet_name)

        wb: Workbook = writer.book
        ws_grafic = wb.add_worksheet("grafico")

        ws_datos = writer.sheets[sheet_name]
        # Rango de estandar

        calculos_graficos(
            ws_grafic,
            wb,
            min_peso,
            max_peso,
            min_ancho,
            max_ancho,
            min_largo,
            max_largo,
            df_fil,
        )

        # 1) Crea los formatos
        ftm_format = wb.add_format(
            {
                "bg_color": "#C6EFCE",  # verde claro (estilo Excel)
            }
        )
        ws_datos.conditional_format(
            "H1:H100000",
            {
                "type": "formula",
                "criteria": f"=AND(ISNUMBER(H1), H1>= {min_peso}, H1 <= {max_peso})",
                "format": ftm_format,
            },
        )

        ws_datos.conditional_format(
            "I1:I100000",
            {
                "type": "formula",
                "criteria": f"=AND(ISNUMBER(I1), I1>= {min_ancho}, I1 <= {max_ancho})",
                "format": ftm_format,
            },
        )

        ws_datos.conditional_format(
            "J1:J100000",
            {
                "type": "formula",
                "criteria": f"=AND(ISNUMBER(J1), J1>= {min_largo}, J1 <= {max_largo})",
                "format": ftm_format,
            },
        )
        # por si lo necesitas
        # ---------- 🔹 AUTOFIT DE COLUMNAS ----------
        for idx, col in enumerate(df_fil.columns):
            # Longitud máxima entre el nombre de la columna y el contenido
            max_len = (
                max(
                    df_fil[col].astype(str).map(len).max(),  # contenido
                    len(str(col)),  # encabezado
                )
                + 2
            )  # pequeño margen
            ws_datos.set_column(idx, idx, max_len)
        # --------------------------------------------
        # Define las letras reales en Excel (solo aquí)
        #   A: fechas, F: peso, I: límite min, J: límite max (ajusta a tu layout)
        chart = graficos(
            wb=wb,
            df=df_fil,
            sheet=sheet_name,
            value_col_letter="H",
            col_min_letter="K",
            col_max_letter="L",
            start_row=2,  # encabezados en fila 1
            margin=10.0,  # +/- 10 para el eje Y
            name="peso",
        )

        chart_2 = graficos(
            wb=wb,
            df=df_fil,
            sheet=sheet_name,
            value_col_letter="I",
            col_min_letter="M",
            col_max_letter="N",
            start_row=2,  # encabezados en fila 1
            margin=10.0,  # +/- 10 para el eje Y
            name="Eloga Ancho",
        )

        chart_3 = graficos(
            wb=wb,
            df=df_fil,
            sheet=sheet_name,
            value_col_letter="J",
            col_min_letter="O",
            col_max_letter="P",
            start_row=2,  # encabezados en fila 1
            margin=10.0,  # +/- 10 para el eje Y
            name="Eloga Largo",
        )

        ws_grafic.insert_chart("I2", chart)
        ws_grafic.insert_chart("Q2", chart_2)
        ws_grafic.insert_chart("I18", chart_3)
        ws_grafic.autofit()
    output.seek(0)
    return output.getvalue()


def graficos(
    *,
    wb,
    df: DataFrame,
    sheet: str,
    value_col_letter: str,
    col_min_letter: str,
    col_max_letter: str,
    start_row: int = 2,
    margin: float = 10.0,
    name: str,
):
    """
    Crea y devuelve un chart de líneas con tres series:
      - Serie principal en `value_col_letter`
      - Límite Mínimo en `col_min_letter`
      - Límite Máximo en `col_max_letter`
    Las categorías se toman de la columna A (fechas).
    El eje Y se fija a [min(columna)-margin, max(columna)+margin] calculado desde el DataFrame,
    usando la letra de Excel (no el nombre).
    """
    chart = wb.add_chart({"type": "line"})

    n_rows = len(df)
    if n_rows <= 0:
        chart.set_title({"name": "Sin datos"})
        return chart

    end_row = start_row + n_rows - 1

    # --- Series (referencias en Excel por letra) ---
    chart.add_series(
        {
            "name": "Peso",
            "categories": f"='{sheet}'!$A${start_row}:$A${end_row}",
            "values": f"='{sheet}'!${value_col_letter}${start_row}:${value_col_letter}${end_row}",
            "line": {"color": "blue"},
        }
    )
    chart.add_series(
        {
            "name": "Límite Mínimo",
            "categories": f"='{sheet}'!$A${start_row}:$A${end_row}",
            "values": f"='{sheet}'!${col_min_letter}${start_row}:${col_min_letter}${end_row}",
            "line": {"color": "red", "dash_type": "dash"},
        }
    )
    chart.add_series(
        {
            "name": "Límite Máximo",
            "categories": f"='{sheet}'!$A${start_row}:$A${end_row}",
            "values": f"='{sheet}'!${col_max_letter}${start_row}:${col_max_letter}${end_row}",
            "line": {"color": "green", "dash_type": "dash"},
        }
    )

    # --- Ejes y título ---
    chart.set_title({"name": f"Control de {name} por Fecha"})
    chart.set_x_axis({"name": "Fecha"})

    # Calcular min/max del eje Y a partir de la letra de Excel
    y_axis_opts = {"name": f"{name}"}
    try:
        idx = _excel_letter_to_index(value_col_letter)
        if 0 <= idx < df.shape[1]:
            serie = pd.to_numeric(df.iloc[:, idx], errors="coerce").dropna()
            if not serie.empty:
                y_min = float(serie.min()) - margin
                y_max = float(serie.max()) + margin
                # Salvaguarda si todos los valores son iguales
                if y_min >= y_max:
                    # añade pequeño delta para que Excel tenga rango visible
                    y_min = y_min - 1.0
                    y_max = y_max + 1.0
                y_axis_opts["min"] = y_min
                y_axis_opts["max"] = y_max
    except Exception as e:
        # Si hay problema con la letra, deja el eje en automático
        # (puedes hacer st.warning(str(e)) si lo usas en Streamlit)
        pass

    chart.set_y_axis(y_axis_opts)

    return chart
