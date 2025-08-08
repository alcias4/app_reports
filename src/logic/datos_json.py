import json
from pathlib import Path


def datos():
    ruta_json = Path(__file__).parent.parent / "config" / "configuracion.json"
    if not ruta_json.exists():
        raise FileNotFoundError(f"❌ Archivo no encontrado: {ruta_json}")

    with open(ruta_json, "r", encoding="utf-8") as config:
        datos = json.load(config)

    return datos
