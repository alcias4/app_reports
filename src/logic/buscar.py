import asyncio
import os
import re

import pandas as pd


async def buscar_hoja(ruta: str, refe: str) -> list[dict[str, str]]:

    conincidencias = []
    for archivo in os.listdir(ruta):

        if archivo.endswith(".xlsx"):
            ruta_completa = os.path.join(ruta, archivo)
            df = pd.ExcelFile(ruta_completa, engine="calamine")

            nombres = df.sheet_names

            for n in nombres:
                if refe in n:
                    conincidencias.append({"excel": archivo, "hoja": n})

    return conincidencias


async def buscar_especiales(ruta: str, refe: str, hojas_especiales: dict[str, str]):
    coincidencias = []
    # Referencia
    # Ejemplo ref ; 100770
    for k, v in hojas_especiales.items():
        ruta_completa = os.path.join(ruta, v)
        df = pd.read_excel(ruta_completa, sheet_name=k, engine="calamine")
        df.columns = df.columns.str.lower()

        if "referencia" in df.columns:
            existe = df["referencia"].str.contains(refe, na=False).any()

            if existe:
                coincidencias.append({"excel": v, "hoja": k})
    return coincidencias


async def buscar(ruta: str, refe: str, hojas_especiales: dict[str, str]):
    resultdados = await asyncio.gather(
        buscar_hoja(ruta, refe),
        buscar_especiales(ruta, refe, hojas_especiales),
    )

    return resultdados
