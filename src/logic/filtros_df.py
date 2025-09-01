import pandas as pd
import streamlit as st
from pandas import DataFrame


def filtros_df(df: DataFrame, fecha: str):
    if fecha != None and fecha != "":
        df[fecha] = pd.to_datetime(df[fecha])

        df["año"] = df[fecha].dt.year
        fil_año = ["Todos"] + sorted(df["año"].dropna().unique().tolist())
        valor_año = st.selectbox("Ingresa años", fil_año, key="años tabla")

        if valor_año != "Todos":
            return df[df["año"] == valor_año]
        else:
            return df
