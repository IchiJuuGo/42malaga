
import os
import sys
import argparse
import datetime as dt
from PIL import Image, ExifTags

if len(sys.argv) == 1:
    print("Debe proporcionar al menos una ruta de imagen para analizar.")
    sys.exit(1)

def verificar_imagen(ruta):
   return os.path.isfile(ruta) and Image.open(ruta)

def analizar_metadatos_imagen(ruta):
    try:
        ultima_modificacion = os.stat(ruta).st_mtime
        fecha_de_creacion = os.stat(ruta).st_ctime

        imagen = Image.open(ruta)
        metadatos = imagen._getexif()

        print(f"{'Abierto':32}: {ruta}")
        print(f"{'Nombre de archivo':32}: {imagen.filename}")
        print(f"{'Dimensiones':32}: {imagen.size[0]}, {imagen.size[1]}")
        print(f"{'Formato':32}: {imagen.format}")
        print(f"{'Modo de color':32}: {imagen.mode}")
        print(f"{'Paleta':32}: {imagen.palette}")
        print(f"{'Fecha de modificación':32}: {dt.datetime.fromtimestamp(ultima_modificacion)}")
        print(f"{'Fecha de creación':32}: {dt.datetime.fromtimestamp(fecha_de_creacion)}")

        if metadatos:
            print(f"{'Metadatos EXIF':32}: {metadatos}\n")
            [print(f"{ExifTags.TAGS.get(tag):32}: {valor}") for tag, valor in metadatos.items()]
        else:
            print(f"{'Metadatos EXIF':32}: No se encontraron metadatos.\n")

        print("-" * 80)
    except Exception as e:
        parser.error(f"No se pudo abrir la imagen: {ruta} ({e})")

parser = argparse.ArgumentParser(description='Análisis de metadatos de imágenes.')
parser.add_argument('ruta', metavar='ruta', type=str, nargs='+', help='Introduce la ruta de la imagen que quieras analizar')

args = parser.parse_args()

for ruta in args.ruta:
    if not verificar_imagen(ruta):
        parser.error(f"No se encontró la imagen en la ruta especificada: {ruta}")

for ruta in args.ruta:
    analizar_metadatos_imagen(ruta)
    