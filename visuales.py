import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import keyboard

# URL de la página web modifique 👇
url = 'URL_DE_LA_PAGINA_WEB'

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
