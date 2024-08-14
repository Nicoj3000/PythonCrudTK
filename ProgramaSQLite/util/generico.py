import os

def crear_carpeta_si_no_existe(ruta, nombre_carpeta):
    ruta_completa = os.path.join(ruta,nombre_carpeta)


    if not os.path.exists(ruta_completa):
        os.makedirs(ruta_completa)
        return True, f"Se ha creado la carpeta {nombre_carpeta} en {ruta}"
    else:
        return False, f"La carpeta {nombre_carpeta} ya existe en {ruta}"