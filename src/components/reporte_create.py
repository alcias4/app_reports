import streamlit as st
from pandas import DataFrame
from rapidfuzz import process

from components.estandares import estand
from logic.generar_excel import generar_excel


def reporte_crear(df: DataFrame):
    min_peso, max_peso, min_ancho, max_ancho, min_largo, max_largo = estand(
        key_prefix="report"
    )
    lista_principal = columnas_coincidencias(df)
    lista_columnas = st.multiselect(
        "Seleccionar columnas adicionales",
        df.columns,
        key="columnas elegir",
        help="Elegir columnas aparte de las que ya estan y se agregaran al final de la tabla",
        placeholder="Ejemplo: mallas...",
    )

    lista_complet = (
        lista_principal + lista_columnas if len(lista_columnas) > 0 else lista_principal
    )

    if lista_complet:
        df_filtrado = df[lista_complet].copy()
        df_filtrado["min_peso"] = min_peso
        df_filtrado["max_peso"] = max_peso
        df_filtrado["min_elog_ancho"] = min_ancho
        df_filtrado["max_elog_ancho"] = max_ancho
        df_filtrado["min_elog_largo"] = min_largo
        df_filtrado["max_elog_largo"] = max_largo
        st.dataframe(df_filtrado, hide_index=True)

        # generar excel

        excel_bytes = generar_excel(
            df_filtrado,
            min_peso=min_peso,
            max_peso=max_peso,
            min_ancho=min_ancho,
            max_ancho=max_ancho,
            min_largo=min_largo,
            max_largo=max_largo,
        )

        st.download_button(
            label="📥 Descargar Excel",
            data=excel_bytes,
            file_name="Reporte_rapido.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
    else:
        st.info("Selecciona al menos una columna para generar el reporte.")


def columnas_coincidencias(df: DataFrame):

    columnas = [
        "fecha",
        "año",
        "demanda",
        "referencia",
        "color",
        "telar",
        "vte",
        "peso",
        "elog ancho",
        "elog largo",
    ]
    columnas_fil = []
    for patron in columnas:
        coincidencias = process.extractOne(patron, list(df.columns), score_cutoff=80)
        if coincidencias:
            columnas_fil.append(coincidencias[0])

    return columnas_fil
