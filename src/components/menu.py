from streamlit_option_menu import option_menu


def menu() -> str:
    resul: str = option_menu(
        menu_title=None,
        options=["Reporte", "Buscar Ref"],
        icons=["graph-up", "search"],
        orientation="horizontal",
    )

    return resul
