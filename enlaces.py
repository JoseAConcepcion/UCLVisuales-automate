import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def encontrar_directorios(url):
    directorios = []  # Lista para almacenar los enlaces completos a directorios

    try:
        response = requests.get(url)
        response.raise_for_status()
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')
        filas = soup.find_all('tr')  

        for fila in filas:
            celdas = fila.find_all('td')

            if celdas and 'alt' in celdas[0].img.attrs and celdas[0].img['alt'] == '[DIR]':
                enlace = celdas[1].a
                if enlace:
                    enlace_completo = urljoin(url, enlace['href'])
                    directorios.append(enlace_completo)

        for directorio in directorios:
            directorios.extend(encontrar_directorios(directorio))

        return directorios

    except requests.exceptions.RequestException as e:
        print(f'Error al obtener la página web: {e}')
        return []
