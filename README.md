# UCLVisuales-automate 💻

## Descargador de Videos desde el repositorio de UCLV 🎥

Este script de Python te permite descargar automáticamente todos los archivos de video con subtitulos, y guardarlos en una carpeta de destino local.

## Requisitos 🛠️

Antes de ejecutar el script, asegúrate de tener Python 3 instalado en tu sistema. También necesitarás instalar los requerimientos. Bastará con ejecutar el siguiente comando:

```bash
pip install -r requirements.txt
```

## Uso 🚀

1. Clona o descarga este repositorio en tu máquina local.

2. Ejecuta el script desde la línea de comandos:

   ```bash
   python visuales.py
   ```

3. El script te preguntará si deseas ingresar las URLs manualmente (1) o desde un archivo (2).

4. Si eliges ingresar las URLs manualmente, simplemente sigue las instrucciones y proporciona las URLs que desees descargar. Para finalizar la entrada, escribe 'fin'.

5. Si eliges cargar las URLs desde un archivo llamado `links.txt` en la misma carpeta que el script, asegúrate de que el archivo exista y contenga las URLs una por línea.

6. El script comenzará a buscar y descargar automáticamente los archivos multimedia desde las URLs proporcionadas.

## Notas 📝

- Puedes ajustar las extensiones permitidas modificando la lista `extensiones_permitidas` en el script si deseas incluir otras extensiones de video.

- La carpeta de destino se creará en el directorio actual donde se encuentra el archivo `.py`.

Disfruta 😃

Si tienes alguna pregunta o problema, no dudes en abrir un problema en este repositorio. 🙋
