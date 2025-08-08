from pandas import DataFrame
from xlsxwriter.workbook import Workbook
from xlsxwriter.worksheet import Worksheet


def cal_adicionales(ws_adicional: Worksheet, wb: Workbook, df_fil: DataFrame):
    fmt_header = wb.add_format(
        {
            "bold": True,
            "bg_color": "#D9E1F2",  # azul claro tipo encabezado
            "align": "center",
            "valign": "vcenter",
            "border": 1,
        }
    )
    ### Correlaciones lineales
    fmt_num3 = wb.add_format({"num_format": "0.000"})

    ws_adicional.write("B1", "Correlación lineal", fmt_header)
    ws_adicional.write("A2", "Correlación peso vs Elogac Ancho", fmt_header)

    correlacion_peso_ancho = df_fil.iloc[:, 7].corr(df_fil.iloc[:, 8], method="pearson")

    ws_adicional.write("B2", correlacion_peso_ancho, fmt_num3)

    ws_adicional.write("A3", "Correlación peso vs Elogac Largo", fmt_header)

    correlacion_peso_largo = df_fil.iloc[:, 7].corr(df_fil.iloc[:, 9], method="pearson")

    ws_adicional.write("B3", correlacion_peso_largo, fmt_num3)

    ws_adicional.write("A4", "Correlación Elog Ancho vs Elogac Largo", fmt_header)

    correlacion_ancho_largo = df_fil.iloc[:, 8].corr(
        df_fil.iloc[:, 9], method="pearson"
    )

    ws_adicional.write("B4", correlacion_ancho_largo, fmt_num3)

    ws_adicional.insert_textbox(
        "D2",  # Celda de referencia (arranque)
        "Si la correlación (pearson) da mayor o igual a 7 o -7 Hay relación fuerte entre esas variables,  si es menor no hay relación lineal",  # Texto
        {
            "width": 250,  # Ancho en píxeles
            "height": 90,  # Alto en píxeles
            "fill": {"color": "#E7ECF7"},  # Color de fondo
            "font": {"name": "Calibri", "size": 11, "color": "black"},  # Fuente
            "align": {"vertical": "middle", "horizontal": "center"},  # Alineación
            "border": {"color": "black"},  # Borde
        },
    )

    ### Correlaciones no lineales spearmean
    ws_adicional.write("B7", "Correlación no lineal o lineal", fmt_header)
    ws_adicional.write("A8", "Correlación peso vs Elogac Ancho", fmt_header)

    correlacion_peso_ancho = df_fil.iloc[:, 7].corr(
        df_fil.iloc[:, 8], method="spearman"
    )

    ws_adicional.write("B8", correlacion_peso_ancho, fmt_num3)

    ws_adicional.write("A9", "Correlación  peso vs Elogac Largo", fmt_header)

    correlacion_peso_largo = df_fil.iloc[:, 7].corr(
        df_fil.iloc[:, 9], method="spearman"
    )

    ws_adicional.write("B9", correlacion_peso_largo, fmt_num3)

    ws_adicional.write("A10", "Correlación  Elog Ancho vs Elogac Largo", fmt_header)

    correlacion_ancho_largo = df_fil.iloc[:, 8].corr(
        df_fil.iloc[:, 9], method="spearman"
    )

    ws_adicional.write("B10", correlacion_ancho_largo, fmt_num3)
    texto_spearman = (
        "Interpretación (Correlación de Spearman)\n"
        "- Valores cercanos a 0: no hay una tendencia clara entre las variables.\n"
        "- Valores cercanos a 1 (o -1): relación fuerte (positiva o negativa).\n"
        "- Spearman detecta relaciones monótonas (pueden ser curvas, no solo rectas).\n"
        "- Estos resultados no implican causalidad, solo asociación.\n"
        "\n"
        "Guía rápida: |ρ| ≥ 0.7 ⇒ fuerte; 0.40–0.69 ⇒ moderada; ≤ 0.39 ⇒ débil."
    )
    ws_adicional.insert_textbox(
        "D8",  # Celda de referencia (arranque)
        texto_spearman,  # Texto
        {
            "width": 420,  # Ancho en píxeles
            "height": 180,  # Alto en píxeles
            "fill": {"color": "#E7ECF7"},  # Color de fondo
            "font": {"name": "Calibri", "size": 11, "color": "black"},  # Fuente
            "align": {"vertical": "middle", "horizontal": "center"},  # Alineación
            "border": {"color": "black"},  # Borde
        },
    )
