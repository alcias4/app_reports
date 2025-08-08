import asyncio
import json

import streamlit as st

from logic.buscar import buscar


def buscar_refe(datos: json):
    ruta = datos["ruta"]
    hojas_especiales = datos["hojas"]

    refe = st.text_input(
        "Ingresa una referencia",
        placeholder="Ej: 100001",
    )

    if st.button("🔍 Buscar referencia") and len(refe) >= 6:
        # Guardar la referencia escrita
        st.session_state["refe_guardada"] = refe

        # Mostrar spinner de carga
        with st.spinner("🔄 Buscando coincidencias, por favor espera..."):
            coincidencias_1, coincidencias_2 = asyncio.run(
                buscar(ruta, refe, hojas_especiales)
            )
            st.session_state["union"] = coincidencias_1 + coincidencias_2

    elif refe != "" and len(refe) < 6:
        st.error("Escribe una referencia válida")

    # Mostrar resultados si ya hay algo en el estado
    if "union" in st.session_state:
        if len(st.session_state["union"]) > 0:
            st.divider()
            st.write(st.session_state["union"])
        else:
            st.warning("¡No existe o no está bien escrito!")
