import pandas as pd
import streamlit as st
from pandas import DataFrame
from rapidfuzz import process

from components.estandares import estand
from logic.cal_complejos import cal_frecuencia


def cal_tendencia(df: DataFrame):

    columnas = ["peso", "elog ancho", "elog largo"]
    columnas_fil = []
    for patron in columnas:
        coincidencias = process.extractOne(patron, list(df.columns), score_cutoff=80)
        if coincidencias:
            columnas_fil.append(coincidencias[0])

    min_peso, max_peso, min_ancho, max_ancho, min_largo, max_largo = estand(
        key_prefix="calculos"
    )

    result_cal_std = cal_frecuencia(
        df, min_peso, max_peso, min_ancho, max_ancho, min_largo, max_largo, columnas_fil
    )

    if result_cal_std:
        st.divider()
        st.subheader("Datos Estadísticos")
        for i, n in enumerate(result_cal_std):
            if n:
                st.subheader(columnas_fil[i])
                # Convertir a DataFrame: una fila con los valores, columnas con los nombres
                df_resumen = pd.DataFrame([n])

                # Reorganizar: dos filas → descripción + valores (si quieres transpuesta)
                df_resumen_transpuesta = df_resumen.T.reset_index()
                df_resumen_transpuesta.columns = ["Descripción", "Valor"]
                st.dataframe(
                    df_resumen_transpuesta, use_container_width=True, hide_index=True
                )
    else:
        st.info("Llena los parametros para poder hacer los cálculos")
