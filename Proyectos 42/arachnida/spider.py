
# Librerias
import os
import sys
import shutil
import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import validators

if len(sys.argv) == 1:
    print("Debe proporcionar al menos una URL para empezar el scrapeo.")
    sys.exit(1)

# Variable global
extensiones = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]

# Funciones definidas
# >> Descarga una imagen desde una URL y la guarda en el archivo especificado,
# ya sea descargándola directamente desde la URL si comienza con "http" o "https"
# o abriendo el archivo local y copiando su contenido en el archivo de salida.
def descargar_imagen_url(url, nombre_archivo):
    if url.startswith(("http", "https")):
        response = requests.get(url)
        with open(nombre_archivo, "wb") as f:
            f.write(response.content)
    else:
        with open(url, "rb") as f, open(nombre_archivo, "wb") as archivo_salida:
            archivo_salida.write(f.read())

# >> Busca todas las imágenes locales en una página web  
# y las copia en una ruta de destino que elijamos.
def descargar_imagen_local(url, path):
    with open(url, "rb") as f:
        contents = f.read()
    soup = BeautifulSoup(contents, features="html.parser")
    for img in soup.find_all("img"):
        img_url = img.attrs.get("src")
        print(img_url)
        if img_url.startswith("http"):
            print("No es una imagen local")
        else:
        # elif not os.path.exists(img_url):
            try:
                shutil.copy(img_url, path)
            except(FileNotFoundError):
                print("Archivo no encontrado")
        if not img_url:
            continue
        # Ignorar imágenes que no tienen una extensión conocida
        if not any(img_url.lower().endswith(ext) for ext in extensiones):
            continue
    # Esta línea imprime la URL de la última imagen en la lista de imágenes extraídas.
    print(img_url)

# >> Recibe una URL de un sitio web, una ruta de destino. 
# La función extrae las imágenes de la página web especificada.
def extraer_imagenes(url, ruta, recursivo, max_profundidad, profundidad_actual=0):
    if profundidad_actual >= max_profundidad:
        return
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    for img in soup.find_all("img"):
        img_url = img.attrs.get("src")
        if img_url and any(img_url.lower().endswith(ext) for ext in extensiones):
            img_url = urljoin(url, img_url)
            nombre_archivo = os.path.join(ruta, os.path.basename(img_url))
            descargar_imagen_url(img_url, nombre_archivo)
            print(f"Descargada la imagen {img_url} en {nombre_archivo}")
    if recursivo:
        for link in soup.find_all("a"):
            link_url = link.attrs.get("href")
            print(link_url)
            if link_url and not link_url.startswith("#") and link_url.startswith("http") and url in link_url and not any(link_url.lower().endswith(ext) for ext in extensiones):
                extraer_imagenes(link_url, ruta, recursivo, max_profundidad, profundidad_actual + 1)

# >> Analiza los argumentos de línea de comandos, valida la URL especificada y realiza la descarga de imágenes 
# desde la URL o el archivo local, según corresponda.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='spider', description='''<Bienvenido a Spider> 
    Spider descarga todas las imágenes de un sitio web en la ruta que elijas.
    Introduce una URL junto con el programa y comencemos.''', 
    usage='%(prog)s [options] url')
    parser.add_argument('url', type=str, help='La URL a escrapear')
    parser.add_argument('-r', '--recursivo', action='store_true', help='Habilitar el escrapeo recursivo')
    parser.add_argument('-l', '--profundidad', metavar='', type=int, choices=[1, 2, 3, 4, 5], default=1, help='Profundidad del escrapeo recursivo (1 a 5)')
    parser.add_argument('-p', '--ruta', metavar='', type=str, default='./data/', help='Ruta para guardar los archivos descargados')

    args = parser.parse_args()

    url = args.url
    recursivo = args.recursivo
    max_profundidad = args.profundidad
    ruta = args.ruta

    if not os.path.exists(ruta):
        os.makedirs(ruta)

    if validators.url(url):
        extraer_imagenes(url, ruta, recursivo, max_profundidad)
        print("Scrapeo web completado")
    elif os.path.exists(url):
        print("Archivo válido")
        if url.endswith(".html"):
            descargar_imagen_local(url, ruta)
        else:
            print("Formato inválido")
            exit()
    else:
        print("URL o ruta de archivo inválida")
        exit()
