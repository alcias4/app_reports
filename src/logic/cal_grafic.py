from pandas import DataFrame
from xlsxwriter.workbook import Workbook
from xlsxwriter.worksheet import Worksheet


def calculos_graficos(
    ws_grafic: Worksheet,
    wb: Workbook,
    min_peso,
    max_peso,
    min_ancho,
    max_ancho,
    min_largo,
    max_largo,
    df_fil: DataFrame,
):
    fmt_header = wb.add_format(
        {
            "bold": True,
            "bg_color": "#D9E1F2",  # azul claro tipo encabezado
            "align": "center",
            "valign": "vcenter",
            "border": 1,
        }
    )

    fmt_pct3 = wb.add_format({"num_format": "0.000%"})  # 3 decimales en porcentaje
    fmt_num3 = wb.add_format({"num_format": "0.000"})

    ws_grafic.write("G5", "todos")

    ws_grafic.write("A1", "Min Peso", fmt_header)
    ws_grafic.write("A2", min_peso)
    ws_grafic.write("B1", "Max Peso", fmt_header)
    ws_grafic.write("B2", max_peso)

    ws_grafic.write("C1", "Min Eloga Ancho", fmt_header)
    ws_grafic.write("C2", min_ancho)
    ws_grafic.write("D1", "Max Elogan Ancho", fmt_header)
    ws_grafic.write("D2", max_ancho)

    ws_grafic.write("E1", "Min Eloga Largo", fmt_header)
    ws_grafic.write("E2", min_largo)
    ws_grafic.write("F1", "Max Eloga Largo", fmt_header)
    ws_grafic.write("F2", max_largo)

    ws_grafic.write("B4", "Cantidad de datos", fmt_header)
    ws_grafic.write("C4", "Porcentaje", fmt_header)
    ws_grafic.write("F4", "Total de datos", fmt_header)
    ws_grafic.write("D4", "Promedio Total", fmt_header)
    ws_grafic.write("G4", "Filtro por año o todos", fmt_header)

    año = "G5"

    # Total de datos
    ws_grafic.write_formula(
        "F5",
        f'=IF({año}="todos",COUNT(datos!A2:A100000),COUNTIFS(datos!B2:B50000,"="&{año}))',
    )

    # Peso dentro de rango
    ws_grafic.write("A5", "Peso que cumplen", fmt_header)
    ws_grafic.write_formula(
        "B5",
        f'=IF({año}="todos",COUNTIFS(datos!H2:H50000,">="&A2,datos!H2:H50000,"<="&B2),'
        f'COUNTIFS(datos!H2:H50000,">="&A2,datos!H2:H50000,"<="&B2,datos!B2:B50000,"="&{año}))',
    )

    # Peso liviano
    ws_grafic.write("A6", "Peso liviano", fmt_header)
    ws_grafic.write_formula(
        "B6",
        f'=IF({año}="todos",COUNTIFS(datos!H2:H50000,"<"&A2),'
        f'COUNTIFS(datos!H2:H50000,"<"&A2,datos!B2:B50000,"="&{año}))',
    )

    # Peso pesado
    ws_grafic.write("A7", "Peso Pesado", fmt_header)
    ws_grafic.write_formula(
        "B7",
        f'=IF({año}="todos",COUNTIFS(datos!H2:H50000,">"&B2),'
        f'COUNTIFS(datos!H2:H50000,">"&B2,datos!B2:B50000,"="&{año}))',
    )

    # Porcentajes peso
    ws_grafic.write_formula("C5", '=IFERROR(B5/F5, "")', fmt_pct3)
    ws_grafic.write_formula("C6", '=IFERROR(B6/F5, "")', fmt_pct3)
    ws_grafic.write_formula("C7", '=IFERROR(B7/F5, "")', fmt_pct3)
    ws_grafic.write_formula("D5", '=IFERROR(AVERAGE(datos!H2:H50000), "")', fmt_num3)

    # Elongación ancho que cumplen
    ws_grafic.write("A9", "Elogaciones Ancho que cumplen", fmt_header)
    ws_grafic.write_formula(
        "B9",
        f'=IF({año}="todos",COUNTIFS(datos!I2:I50000,">="&C2,datos!I2:I50000,"<="&D2),'
        f'COUNTIFS(datos!I2:I50000,">="&C2,datos!I2:I50000,"<="&D2,datos!B2:B50000,"="&{año}))',
    )

    ws_grafic.write("A10", "Eloga Ancho por debajo", fmt_header)
    ws_grafic.write_formula(
        "B10",
        f'=IF({año}="todos",COUNTIFS(datos!I2:I50000,"<"&C2),'
        f'COUNTIFS(datos!I2:I50000,"<"&C2,datos!B2:B50000,"="&{año}))',
    )

    ws_grafic.write("A11", "Elon Ancho Por arriba", fmt_header)
    ws_grafic.write_formula(
        "B11",
        f'=IF({año}="todos",COUNTIFS(datos!I2:I50000,">"&D2),'
        f'COUNTIFS(datos!I2:I50000,">"&D2,datos!B2:B50000,"="&{año}))',
    )

    ws_grafic.write_formula("C9", '=IFERROR(B9/F5, "")', fmt_pct3)
    ws_grafic.write_formula("C10", '=IFERROR(B10/F5, "")', fmt_pct3)
    ws_grafic.write_formula("C11", '=IFERROR(B11/F5, "")', fmt_pct3)
    ws_grafic.write_formula("D9", '=IFERROR(AVERAGE(datos!I2:I50000), "")', fmt_num3)

    # Elongación largo
    ws_grafic.write("A13", "Elogaciones Largo que cumplen", fmt_header)
    ws_grafic.write_formula(
        "B13",
        f'=IF({año}="todos",COUNTIFS(datos!J2:J50000,">="&E2,datos!J2:J50000,"<="&F2),'
        f'COUNTIFS(datos!J2:J50000,">="&E2,datos!J2:J50000,"<="&F2,datos!B2:B50000,"="&{año}))',
    )

    ws_grafic.write("A14", "Eloga Largo por debajo", fmt_header)
    ws_grafic.write_formula(
        "B14",
        f'=IF({año}="todos",COUNTIFS(datos!J2:J50000,"<"&E2),'
        f'COUNTIFS(datos!J2:J50000,"<"&E2,datos!B2:B50000,"="&{año}))',
    )

    ws_grafic.write("A15", "Elon Largo Por arriba", fmt_header)
    ws_grafic.write_formula(
        "B15",
        f'=IF({año}="todos",COUNTIFS(datos!J2:J50000,">"&F2),'
        f'COUNTIFS(datos!J2:J50000,">"&F2,datos!B2:B50000,"="&{año}))',
    )

    ws_grafic.write_formula("C13", '=IFERROR(B13/F5, "")', fmt_pct3)
    ws_grafic.write_formula("C14", '=IFERROR(B14/F5, "")', fmt_pct3)
    ws_grafic.write_formula("C15", '=IFERROR(B15/F5, "")', fmt_pct3)
    ws_grafic.write_formula("D13", '=IFERROR(AVERAGE(datos!J2:J50000), "")', fmt_num3)
