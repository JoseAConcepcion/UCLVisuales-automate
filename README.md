# UCLVisuales-automate 💻

## Descargador de Videos desde el repositorio de UCLV ⬇️

Este script de Python te permite descargar automáticamente todos los archivos de video con extensiones `.mp4` o `.mkv`, y guardarlos en una carpeta de destino local.

## Requisitos 🛠️

Antes de ejecutar el script, asegúrate de tener Python 3 instalado en tu sistema. También necesitarás instalar las siguientes bibliotecas de Python si aún no las tienes:

```bash
pip install requests
pip install beautifulsoup4
pip install tqdm
```

## Uso 🚀

1. Clona o descarga este repositorio en tu máquina local.

2. Abre el archivo `visuales.py` en un editor de texto y edita las siguientes líneas:

   - `url`: Reemplaza `'URL_DE_LA_PAGINA_WEB'` con la URL de la página web desde la cual deseas descargar los videos.
   - `carpeta_destino`: Reemplaza `'carpeta_destino'` con la ruta de la carpeta donde deseas guardar los archivos de video.

3. Ejecuta el script desde la línea de comandos:

   ```bash
   python visuales.py
   ```

4. El script comenzará a buscar y descargar automáticamente los archivos de video con extensiones `.mp4` o `.mkv` desde la página web proporcionada.

## Notas 📝

- Puedes ajustar las extensiones permitidas modificando la lista `extensiones_permitidas` en el script si deseas incluir otras extensiones de video.

- La carpeta de destino se creará en el directorio actual donde se encuentra el archivo `.py`.

Disfruta 😃

Si tienes alguna pregunta o problema, no dudes en abrir un problema en este repositorio. 🙋
