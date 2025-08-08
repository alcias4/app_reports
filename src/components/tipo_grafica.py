import plotly.express as px
import streamlit as st
from pandas import DataFrame


def linea(df, x, y, min, max, hover):
    fig = px.line(df, x=x, y=y, hover_data=hover)
    if min != 0 and min != "":
        fig.add_hline(
            y=int(min),
            line_color="red",
            annotation=dict(text="min", font_size=12, font_color="red"),
        )
    if max != 0 and max != "":
        fig.add_hline(
            y=int(max),
            line_color="yellow",
            annotation=dict(text="max", font_size=12, font_color="yellow"),
        )

    st.plotly_chart(fig)


def barras(df: DataFrame, x, y):
    df = df.head(20)
    fig = px.bar(df, x=x, y=y)
    fig.update_layout(yaxis_range=[min(df[y]) - 30, max(df[y]) + 30])
    st.plotly_chart(fig)


def histrograma(df, y):
    fig = px.histogram(df, y=y)

    st.plotly_chart(fig)


def puntos(df: DataFrame, x, y, hover, min, max):
    fig = px.scatter(df, x, y, hover_data=hover)
    if min != 0 and min != "":
        fig.add_hline(
            y=int(min),
            line_color="red",
            annotation=dict(text="min", font_size=12, font_color="red"),
        )
    if max != 0 and max != "":
        fig.add_hline(
            y=int(max),
            line_color="yellow",
            annotation=dict(text="max", font_size=12, font_color="yellow"),
        )

    st.plotly_chart(fig)
