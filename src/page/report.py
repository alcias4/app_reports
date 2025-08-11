import os

import pandas as pd
import streamlit as st

from components.analisis import analisis
from components.grafica import grafica_filtro
from components.reporte_create import reporte_crear


def reporte_general(datos):

    st.title("Reporte General")

    ruta = datos["ruta"]

    lista_archivo = os.listdir(ruta)

    excel_archivo = st.selectbox("Archivo de excel", lista_archivo, index=12)

    df_names = pd.ExcelFile(os.path.join(ruta, excel_archivo), engine="calamine")

    hoja = st.selectbox("Elige una hoja de calculo: ", df_names.sheet_names)

    if excel_archivo and hoja:

        try:
            df = pd.read_excel(
                os.path.join(ruta, excel_archivo),
                sheet_name=hoja,
                engine="calamine",
            )
            df.columns = df.columns.str.replace("\n", " ", regex=False)
            df.columns = df.columns.str.lower()

            if not df.empty:

                estandares = {
                    n: int(df[n][0]) for n in df.columns if "min" in n or "max" in n
                }
                for col in df.columns:
                    tipos = df[col].map(type).unique()
                    if len(tipos) > 1:
                        df[col] = df[col].astype(str)
                st.dataframe(df)
                st.subheader("Parametros Estandar")
                st.write(
                    "Orden de parametros: peso, elongaciones a lo ancho y luego alogaciones  a lo largo"
                )

                if len(estandares) > 0:
                    st.dataframe(pd.DataFrame([estandares]), hide_index=True)
                else:
                    st.info("No estan los estandares en la excel toca bucar por now!")
            else:
                st.warning("Elige otra hoja de cálculo")
        except:
            print("Error en  la creación de la tabla")

        tab_grafica, tab_resum, crear_reporte = st.tabs(
            ["Gráficas", "Análisis  Clásico", "Crear Reporte"]
        )

        if not df.empty:
            with tab_grafica:
                grafica_filtro(df)
            with tab_resum:
                analisis(df)
            with crear_reporte:
                reporte_crear(df)
