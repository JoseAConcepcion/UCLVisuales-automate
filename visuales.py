import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import keyboard

# URL de la página web modifique 👇
url = 'URL_DE_LA_PAGINA_WEB'

def obtener_url_manualmente():
    while True:
        origen_url = input("¿Deseas ingresar la URL manualmente (1) o desde un archivo (2)? ")
        if origen_url == '1':
            url = input("Introduce la URL de la página web: ")
            return url
        elif origen_url == '2':
            archivo_url = 'links.txt'
            try:
                with open(archivo_url, 'r') as archivo:
                    url = archivo.read().strip()
                return url
            except FileNotFoundError:
                print("El archivo 'links.txt' no se encontró en la misma carpeta del script.")
        else:
            print("Respuesta no válida. Debes seleccionar '1' o '2'.")

# Pregunta al usuario por el modo (automático o manual)
while True:
    modo = input("Elige el modo (1 para automático, 2 para manual, ESC para salir): ")
    if modo == '1':
        # Define la URL de la página web en modo automático
        url = 'URL_DE_LA_PAGINA_WEB_AUTOMÁTICA'
        break
    elif modo == '2':
        # Obtiene la URL manualmente
        url = obtener_url_manualmente()
        if url:
            break
    elif modo.lower() == 'esc':
        exit(0)
    else:
        print("Respuesta no válida. Debes seleccionar '1' o '2', o presionar ESC para salir.")

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print('La página web no es accesible, excepción: ')
    print(f'{e}')
    exit(1)

carpeta_destino = os.path.join(os.getcwd(), 'carpeta_destino')

if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

enlaces_video = soup.find_all('a', href=True)

extensiones_permitidas = ['.mp4', '.mkv']

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

print('Descarga de archivos de video completada.')


#! Si el link esta caido por alguna razon o no es accesible y se debe reportar

#todo Necesito un menu para escoger distintas opciones

#todo Se debe dar una lista de todos los links encontrados numerados y se debe preguntar cuales descargar

#todo La respuesta debe ser de por rangos 

#todo Se debe separar el codigo para mas legibilidad

#todo Se debe poder dejar una lista con diferentes links para decargarlos todos

#todo Se debe dejar un modo tipo descargar todo de una lista de links(videos, srt)

#todo se debe dejar un modo manual y otro automatico

#todo se debe sacar los links de un txt

#todo hacer un txt con requirements


#? Ver como implementar lo de abajo


# carpeta_destino = os.path.join(os.getcwd(), 'carpeta_destino')

# if not os.path.exists(carpeta_destino):
#     os.makedirs(carpeta_destino)

# # Verifica si la página web está accesible
# try:
#     response = requests.get(url)
#     response.raise_for_status()  # Lanza una excepción si la solicitud no tiene éxito
# except requests.exceptions.RequestException as e:
#     print(f'La página web no está accesible: {e}')
#     exit(1)  # Termina el script con un código de error

# # Resto del script (descarga de archivos de video) sigue igual
