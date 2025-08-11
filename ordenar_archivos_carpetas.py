import os
import shutil

# Ruta donde están tus archivos
ruta = "/home/ivanlinux/Descargas/"

# Carpetas que vas a usar para clasificar
tipos = ['Imagenes', 'PY', 'Zip', 'Docs', 'PDF', 'CSV', 'Otros']

# Crear carpetas si no existen
for carpeta in tipos:
    ruta_carpeta = os.path.join(ruta, carpeta)
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

# Clasificar y mover archivos
for archivo in os.listdir(ruta):
    ruta_archivo = os.path.join(ruta, archivo)

    # Saltar carpetas (incluyendo las que tú mismo creaste)
    if os.path.isdir(ruta_archivo):
        continue

    # Clasificación por extensión
    if archivo.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
        destino = os.path.join(ruta, 'Imagenes', archivo)
    elif archivo.lower().endswith('.py'):
        destino = os.path.join(ruta, 'PY', archivo)
    elif archivo.lower().endswith('.zip'):
        destino = os.path.join(ruta, 'Zip', archivo)
    elif archivo.lower().endswith('.pdf'):
        destino = os.path.join(ruta, 'PDF', archivo)
    elif archivo.lower().endswith(('.doc', '.docx', '.txt', '.odt')):
        destino = os.path.join(ruta, 'Docs', archivo)
    elif archivo.lower().endswith('.csv'):
        destino = os.path.join(ruta, 'CSV', archivo)
    else:
        destino = os.path.join(ruta, 'Otros', archivo)

    # Mover archivo
    try:
        shutil.move(ruta_archivo, destino)
        print(f"Movido: {archivo} -> {destino}")
    except Exception as e:
        print(f"Error al mover {archivo}: {e}")
