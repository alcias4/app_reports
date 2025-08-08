import pandas as pd
import streamlit as st
from pandas import DataFrame

from components.tipo_grafica import barras, histrograma, linea, puntos


def grafica_filtro(df: DataFrame):
    if df is not None and not df.empty:

        col_x, col_y = st.columns(2)
        with col_x:

            if df.columns[0] != "fecha":
                x = st.selectbox("Eje x", df.columns, index=1)
            else:
                x = st.selectbox("Eje x", df.columns)
        with col_y:
            y = st.selectbox("Eje y", df.columns, index=7)

        hover = st.multiselect(
            "Información extras al pasar por el mouse dentro del gráfico",
            df.columns,
            placeholder="Referencia, Color,...",
        )

        col1, col2 = st.columns(2)

        with col1:
            min = st.text_input(
                "Ingrese el valor min",
                placeholder="Ej: 134",
            )
        with col2:
            max = st.text_input("Ingrese el valor maximo", placeholder="Ej: 154")

        # Filtrados respuesta

        df_filtrado = filtros(df.copy(), fecha=x)

        # tipo de grafico

        opcion_graf = st.radio(
            "Elige tipo de gráfico",
            ["linea", "puntos", "histograma"],
            horizontal=True,
            index=0,
        )

        if opcion_graf == "linea":
            linea(df_filtrado, x, y, min, max, hover)

        elif opcion_graf == "histograma":
            histrograma(df_filtrado, y)

        elif opcion_graf == "puntos":
            puntos(df_filtrado, x, y, hover, min, max)


def filtros(df: DataFrame, fecha: str):

    if fecha != None and fecha != "":
        df[fecha] = pd.to_datetime(df[fecha])
        df["año"] = df[fecha].dt.year
        fil_año = ["Todos"] + sorted(df["año"].dropna().unique().tolist())
        valor_año = st.selectbox("Ingresa años", fil_año)

        if valor_año != "Todos":
            return df[df["año"] == valor_año]
        else:
            return df
