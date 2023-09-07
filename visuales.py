import os
import requests
import keyboard
from bs4 import BeautifulSoup
from tqdm import tqdm

def banner():
    # App banner
    banner_ascii = """
  _   _  ____ _ __     ___                 _           
 | | | |/ ___| |\ \   / (_)___ _   _  __ _| | ___  ___ 
 | | | | |   | | \ \ / /| / __| | | |/ _` | |/ _ \/ __|
 | |_| | |___| |__\ V / | \__ \ |_| | (_| | |  __/\__ \\
  \___/ \____|_____\_/  |_|___/\__,_|\__,_|_|\___||___/
                                                       
"""
    return banner_ascii

# Inicio
print(banner())
print("Presione CTRL + C para cancelar en cualquier momento")
manual = False



def obtener_urls():
    global manual
    while True:
        origen_url = input("¿Deseas el modo manual (1) o automático desde un archivo (2)? ")
        if origen_url == '1':
            urls = []
            manual = True
            while True:
                url = input("Introduce la URL de la página web: ")
                if url.lower() == 'fin':
                    return urls
                try:
                    response = requests.get(url)
                    response.raise_for_status()
                    print('Web Valida')
                except requests.exceptions.RequestException as e:
                    print('La página web no es accesible, excepción: ')
                    print(f'{e}')
                    continue
                urls.append(url)
                continue
        elif origen_url == '2':
            archivo_url = 'links.txt'
            urls = []
            try:
                with open(archivo_url, 'r') as archivo:
                    txt = [line.strip() for line in archivo.readlines() if line.strip()]
                for url in txt:
                    try:
                        response = requests.get(url)
                        response.raise_for_status()
                        urls.append(url)
                    except requests.exceptions.RequestException as e:
                        print(f'La página web \n\n {url} \n\nno es accesible, excepción:\n {e} \n')
                        continue
                return urls
            except FileNotFoundError:
                print("El archivo 'links.txt' no se encontró en la misma carpeta del script.")
        else:
            print("Respuesta no válida. Debes seleccionar '1' o '2'.")
    return urls

urls = obtener_urls()


# extensiones a descargar, modificar según necesidades
extensiones_permitidas = ['.mp4', '.mkv', '.avi', '.srt', '.vtt']

if(manual):
    modificar = input('¿Deseas modificar las extenciones (S/N)? ')
    if modificar.lower() == 's':
        print('Recuerde poner el . antes del formato y teclee fin para terminar')
        extensiones = []
        while True:
            text = input('Extensión que desea: ')
            if text.lower() == 'fin': break
            extensiones.append(text)
        extensiones_permitidas = extensiones


carpeta_destino = os.path.join(os.getcwd(), 'carpeta_destino')

if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)


for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    enlaces_video = soup.find_all('a', href=True)

    for enlace in enlaces_video:
        nombre_archivo = enlace['href']
        if any(nombre_archivo.endswith(ext) for ext in extensiones_permitidas):
            url_archivo = url + nombre_archivo
            archivo_destino = os.path.join(carpeta_destino, nombre_archivo)

            print(f'Descargando: {nombre_archivo}')

            with requests.get(url_archivo, stream=True) as response:
                total_size = int(response.headers.get('content-length', 0))
                block_size = 1024
                t = tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024)

                with open(archivo_destino, 'wb') as archivo_local:
                    for data in response.iter_content(block_size):
                        t.update(len(data))
                        archivo_local.write(data)

                t.close()

            print(f'Archivo {nombre_archivo} descargado con éxito en {archivo_destino}')

print('¡Terminado!')

