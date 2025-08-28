from pandas import DataFrame
from xlsxwriter import Workbook
from xlsxwriter.worksheet import Worksheet


def conteo_categorico(
    df: DataFrame,
    wb: Workbook,
    min_peso: float,
    max_peso: float,
    min_ancho: float,
    max_ancho: float,
    min_largo: float,
    max_largo: float,
):
    columna_peso = 7
    columna_ancho = 8
    columna_largo = 9
    columna_color = 4
    columna_telar = 5
    columnas_vte = 6

    ws = wb.add_worksheet("tablas")

    ### Peso tablas
    tabla_cumple(
        df,
        min_peso,
        max_peso,
        wb,
        "Color que cumple peso",
        columna_peso,
        columna_color,
        ws,
        ["A1", "B1", "C1", "D1"],
        ["A", "B", "C"],
    )
    tabla_no_cumple(
        df,
        min_peso,
        max_peso,
        wb,
        "Color que NO cumple peso",
        columna_peso,
        columna_color,
        ws,
        ["F1", "G1", "H1", "I1"],
        ["F", "G", "H"],
    )

    ## Eloganción ancho
    tabla_cumple(
        df,
        min_ancho,
        max_ancho,
        wb,
        "Color que cumple elognaciónes ancho",
        columna_ancho,
        columna_color,
        ws,
        ["K1", "L1", "M1", "N1"],
        ["K", "L", "M"],
    )
    tabla_no_cumple(
        df,
        min_ancho,
        max_ancho,
        wb,
        "Color que NO cumple elogaciones ancho",
        columna_ancho,
        columna_color,
        ws,
        ["P1", "Q1", "R1", "S1"],
        ["P", "Q", "R"],
    )
    ### Columna Elogaciones largo
    tabla_cumple(
        df,
        min_largo,
        max_largo,
        wb,
        "Color que cumple elognaciónes ancho",
        columna_largo,
        columna_color,
        ws,
        ["U1", "V1", "W1", "X1"],
        ["U", "V", "W"],
    )
    tabla_no_cumple(
        df,
        min_largo,
        max_largo,
        wb,
        "Color que NO cumple elogaciones ancho",
        columna_largo,
        columna_color,
        ws,
        ["Z1", "AA1", "AB1", "AC1"],
        ["Z", "AA", "AB"],
    )

    #### Telar

    ### Peso tablas
    tabla_cumple(
        df,
        min_peso,
        max_peso,
        wb,
        "Color que cumple peso",
        columna_peso,
        columna_telar,
        ws,
        ["AE1", "AF1", "AG1", "AH1"],
        ["AE", "AF", "AH"],
    )
    tabla_no_cumple(
        df,
        min_peso,
        max_peso,
        wb,
        "Color que NO cumple peso",
        columna_peso,
        columna_color,
        ws,
        ["F1", "G1", "H1", "I1"],
        ["F", "G", "H"],
    )

    ## Eloganción ancho
    tabla_cumple(
        df,
        min_ancho,
        max_ancho,
        wb,
        "Color que cumple elognaciónes ancho",
        columna_ancho,
        columna_color,
        ws,
        ["K1", "L1", "M1", "N1"],
        ["K", "L", "M"],
    )
    tabla_no_cumple(
        df,
        min_ancho,
        max_ancho,
        wb,
        "Color que NO cumple elogaciones ancho",
        columna_ancho,
        columna_color,
        ws,
        ["P1", "Q1", "R1", "S1"],
        ["P", "Q", "R"],
    )
    ### Columna Elogaciones largo
    tabla_cumple(
        df,
        min_largo,
        max_largo,
        wb,
        "Color que cumple elognaciónes ancho",
        columna_largo,
        columna_color,
        ws,
        ["U1", "V1", "W1", "X1"],
        ["U", "V", "W"],
    )
    tabla_no_cumple(
        df,
        min_largo,
        max_largo,
        wb,
        "Color que NO cumple elogaciones ancho",
        columna_largo,
        columna_color,
        ws,
        ["Z1", "AA1", "AB1", "AC1"],
        ["Z", "AA", "AB"],
    )

    ws.autofit()


def tabla_cumple(
    df: DataFrame,
    min: float,
    max: float,
    wb: Workbook,
    texto_titulo: str,
    columna: int,
    columna_obj: int,
    ws: Worksheet,
    columnas_letras: list[str],
    filas_letras: list[str],
):
    # Ws

    fmt_header = wb.add_format(
        {
            "bold": True,
            "bg_color": "#D9E1F2",  # azul claro tipo encabezado
            "align": "center",
            "valign": "vcenter",
            "border": 1,
        }
    )

    fmt_celda = wb.add_format({"align": "center", "valign": "vcenter", "border": 1})

    # Colores
    columna_color = (
        df[(df.iloc[:, columna] >= min) & (df.iloc[:, columna] <= max)]
        .iloc[:, columna_obj]
        .value_counts()
        .sort_values(ascending=False)
    )

    total_color = df.iloc[:, columna_obj].count()
    # first row, first colum, last_row, last_colum

    ws.write(columnas_letras[0], texto_titulo, fmt_header)
    ws.write(columnas_letras[1], "Cantidad", fmt_header)
    ws.write(columnas_letras[2], "Porcentajes (%)", fmt_header)

    celda_inico = 2
    for color, cantidad in columna_color.items():

        ws.write(f"{filas_letras[0]}{celda_inico}", color, fmt_celda)
        ws.write(f"{filas_letras[1]}{celda_inico}", cantidad, fmt_celda)
        ws.write(
            f"{filas_letras[2]}{celda_inico}",
            round((cantidad / total_color) * 100, 3),
            fmt_celda,
        )

        celda_inico += 1


def tabla_no_cumple(
    df: DataFrame,
    min: float,
    max: float,
    wb: Workbook,
    texto_titulo: str,
    columna: int,
    columna_obj: int,
    ws: Worksheet,
    columnas_letras: list[str],
    filas_letras: list[str],
):
    # Ws

    fmt_header = wb.add_format(
        {
            "bold": True,
            "bg_color": "#D9E1F2",  # azul claro tipo encabezado
            "align": "center",
            "valign": "vcenter",
            "border": 1,
        }
    )

    fmt_celda = wb.add_format({"align": "center", "valign": "vcenter", "border": 1})

    # Colores
    columna_color = (
        df[(df.iloc[:, columna] < min) | (df.iloc[:, columna] > max)]
        .iloc[:, columna_obj]
        .value_counts()
        .sort_values(ascending=False)
    )

    total_color = df.iloc[:, columna_obj].count()
    # first row, first colum, last_row, last_colum

    ws.write(columnas_letras[0], texto_titulo, fmt_header)
    ws.write(columnas_letras[1], "Cantidad", fmt_header)
    ws.write(columnas_letras[2], "Porcentajes (%)", fmt_header)

    celda_inico = 2
    for color, cantidad in columna_color.items():

        ws.write(f"{filas_letras[0]}{celda_inico}", color, fmt_celda)
        ws.write(f"{filas_letras[1]}{celda_inico}", cantidad, fmt_celda)
        ws.write(
            f"{filas_letras[2]}{celda_inico}",
            round((cantidad / total_color) * 100, 3),
            fmt_celda,
        )

        celda_inico += 1
