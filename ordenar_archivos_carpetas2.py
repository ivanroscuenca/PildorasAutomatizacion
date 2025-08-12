import os
import shutil

from tkinter import Tk,filedialog

ventana = Tk()
ventana.withdraw()
ruta=filedialog.askdirectory(title='Seleccione la carpeta a ordenar')



# Ruta donde están tus archivos
ruta = "/home/ivanlinux/Descargas/"

# Diccionario con las extensiones y su carpeta correspondiente
extensiones = {
    'Imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'PY': ['.py'],
    'Zip': ['.zip'],
    'PDF': ['.pdf'],
    'Docs': ['.doc', '.docx', '.txt', '.odt'],
    'CSV': ['.csv'],
}

# Crear las carpetas si no existen
for carpeta in extensiones.keys():
    ruta_carpeta = os.path.join(ruta, carpeta)
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

# Mover archivos a sus carpetas
for archivo in os.listdir(ruta):
    ruta_archivo = os.path.join(ruta, archivo)
    if os.path.isfile(ruta_archivo):
        nombre, ext = os.path.splitext(archivo)
        ext = ext.lower()
        for carpeta, lista_ext in extensiones.items():
            if ext in lista_ext:
                destino = os.path.join(ruta, carpeta, archivo)
                shutil.move(ruta_archivo, destino)
                break
