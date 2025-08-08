import uuid
from typing import Tuple

import streamlit as st


def estand(
    key_prefix: str = "estand",
) -> Tuple[float, float, float, float, float, float]:
    # Tres pares de columnas
    peso_min_col, peso_max_col = st.columns(2)
    ancho_min_col, ancho_max_col = st.columns(2)
    largo_min_col, largo_max_col = st.columns(2)

    with peso_min_col:
        min_peso = st.number_input(
            "Peso Min",
            value=0.0,
            step=0.1,
            key=f"{key_prefix}_peso_min",
            help="Valor mínimo estandar permitido para el peso",
        )

    with peso_max_col:
        max_peso = st.number_input(
            "Peso max",
            value=0.0,
            step=0.1,
            key=f"{key_prefix}_peso_max",
            help="Valor máximo estandar permitido para el peso",
        )

    with ancho_min_col:
        min_ancho = st.number_input(
            "Elongación ancho Min",
            value=0.0,
            step=0.1,
            key=f"{key_prefix}_ancho_min",
            help="valor mínimo estandar de elogaciones a lo ancho",
        )

    with ancho_max_col:
        max_ancho = st.number_input(
            "Elongación ancho max",
            value=0.0,
            step=0.1,
            key=f"{key_prefix}_ancho_max",
            help="valor máximo estandar de elogaciones a lo ancho",
        )

    with largo_min_col:
        min_largo = st.number_input(
            "Elongación largo Min",
            value=0.0,
            step=0.1,
            key=f"{key_prefix}_largo_min",
            help="valor mínimo estandar de elogaciones a lo largo",
        )

    with largo_max_col:
        max_largo = st.number_input(
            "Elongación largo max",  # (quité el doble espacio del label)
            value=0.0,
            step=0.1,
            key=f"{key_prefix}_largo_max",
            help="valor máximo  estandar de elogaciones a lo largo",
        )

    return min_peso, max_peso, min_ancho, max_ancho, min_largo, max_largo

    return min_peso, max_peso, min_ancho, max_ancho, min_largo, max_largo
