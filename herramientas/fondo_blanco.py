"""Cambia el fondo de las fotos de portada por un color liso, sin tocar nada más.

Uso:
    pip install "rembg[cpu]"
    python3 herramientas/fondo_blanco.py portadas.tsv salida/ [--fondo FBF8F4]

portadas.tsv: una línea por producto -> <handle>\t<url de la imagen de portada>
Genera salida/<handle>.jpg con el mismo tamaño y encuadre que la original:
no recorta, no reescala y no mueve el producto; solo sustituye el fondo.

Cada línea de salida lleva "dudoso=N%": la parte del fondo eliminado cuyo color
no se parece al fondo original. Si es alto, revisa esa foto a mano: puede que
el modelo haya borrado algo del producto.
"""
import argparse
import io
import urllib.request
from pathlib import Path

import numpy as np
import onnxruntime as ort
from PIL import Image, ImageOps
from rembg import new_session, remove

MODELO = "birefnet-general"  # respeta mejor prendas claras, piernas y accesorios que isnet


def abrir(datos: bytes, fondo: tuple) -> Image.Image:
    imagen = ImageOps.exif_transpose(Image.open(io.BytesIO(datos)))  # en GIF, primer fotograma
    if imagen.mode in ("RGBA", "LA", "P"):
        imagen = imagen.convert("RGBA")
        lienzo = Image.new("RGBA", imagen.size, fondo + (255,))
        imagen = Image.alpha_composite(lienzo, imagen)
    return imagen.convert("RGB")


def procesar(imagen: Image.Image, fondo: tuple, sesion) -> tuple[Image.Image, float]:
    alfa = np.asarray(remove(imagen, session=sesion, only_mask=True), np.float32)[..., None] / 255
    px = np.asarray(imagen, np.float32)
    resultado = px * alfa + np.array(fondo, np.float32) * (1 - alfa)

    borde = max(4, min(imagen.size) // 33)
    marco = np.concatenate([px[:borde].reshape(-1, 3), px[-borde:].reshape(-1, 3),
                            px[:, :borde].reshape(-1, 3), px[:, -borde:].reshape(-1, 3)])
    distancia = np.linalg.norm(px - np.median(marco, axis=0), axis=2)
    quitado = alfa[..., 0] < 0.5
    dudoso = (quitado & (distancia > 60)).sum() / max(1, (~quitado).sum())

    return Image.fromarray(resultado.round().astype(np.uint8)), 100 * dudoso


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("lista")
    p.add_argument("salida")
    p.add_argument("--fondo", default="FFFFFF", help="color hexadecimal, p. ej. FBF8F4")
    args = p.parse_args()
    fondo = tuple(int(args.fondo.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))

    destino = Path(args.salida)
    destino.mkdir(parents=True, exist_ok=True)
    opciones = ort.SessionOptions()
    opciones.enable_cpu_mem_arena = False  # sin esto birefnet acumula memoria imagen tras imagen
    opciones.enable_mem_pattern = False
    sesion = new_session(MODELO, sess_opts=opciones)
    for linea in Path(args.lista).read_text().splitlines():
        if not linea.strip():
            continue
        handle, url = linea.split("\t")
        archivo = destino / f"{handle}.jpg"
        if archivo.exists():
            continue
        try:
            with urllib.request.urlopen(url) as r:
                imagen, dudoso = procesar(abrir(r.read(), fondo), fondo, sesion)
            imagen.save(archivo, "JPEG", quality=95, subsampling=0)
            print(f"ok {handle} dudoso={dudoso:.1f}%", flush=True)
        except Exception as e:
            print("ERROR", handle, e, flush=True)


if __name__ == "__main__":
    main()
