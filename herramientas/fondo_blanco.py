"""Quita el fondo de las fotos de portada y las pone sobre fondo blanco.

Uso:
    pip install "rembg[cpu]"
    python3 herramientas/fondo_blanco.py portadas.tsv salida/

portadas.tsv: una línea por producto -> <handle>\t<url de la imagen de portada>
Genera salida/<handle>.jpg: cuadrado 2048x2048, fondo #FFFFFF, producto centrado.
"""
import io
import sys
import urllib.request
from pathlib import Path

from PIL import Image
from rembg import new_session, remove

LADO = 2048
MARGEN = 0.08  # 8 % de aire alrededor del producto
FONDO = (255, 255, 255)


def procesar(datos: bytes, sesion) -> Image.Image:
    recorte = remove(Image.open(io.BytesIO(datos)).convert("RGB"), session=sesion)
    recorte = recorte.crop(recorte.getbbox())
    util = int(LADO * (1 - 2 * MARGEN))
    escala = min(util / recorte.width, util / recorte.height)
    recorte = recorte.resize((round(recorte.width * escala), round(recorte.height * escala)), Image.LANCZOS)
    lienzo = Image.new("RGB", (LADO, LADO), FONDO)
    lienzo.paste(recorte, ((LADO - recorte.width) // 2, (LADO - recorte.height) // 2), recorte)
    return lienzo


def main(lista: str, salida: str) -> None:
    destino = Path(salida)
    destino.mkdir(parents=True, exist_ok=True)
    sesion = new_session("isnet-general-use")
    for linea in Path(lista).read_text().splitlines():
        if not linea.strip():
            continue
        handle, url = linea.split("\t")
        archivo = destino / f"{handle}.jpg"
        if archivo.exists():
            continue
        try:
            with urllib.request.urlopen(url) as r:
                procesar(r.read(), sesion).save(archivo, "JPEG", quality=92)
            print("ok", handle)
        except Exception as e:
            print("ERROR", handle, e)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
