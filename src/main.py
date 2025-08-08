import streamlit as st

from components.menu import menu
from logic.datos_json import datos
from page.buscar import buscar_refe
from page.report import reporte_general


def windows():

    datos_json = datos()

    pagina = menu()

    if pagina == "Buscar Ref":
        buscar_refe(datos=datos_json)
    elif pagina == "Reporte":
        reporte_general(datos_json)


windows()
