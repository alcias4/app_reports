import pandas as pd
import streamlit as st
from pandas import DataFrame

from components.calculos import cal_tendencia
from logic.filtros_df import filtros_df


def analisis(df: DataFrame):

    df.columns = df.columns.str.lower()
    fecha = "fecha"

    df_fil = filtros_df(df, fecha)

    cal_tendencia(df_fil)
