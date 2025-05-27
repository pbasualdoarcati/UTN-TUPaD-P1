import re
def limpiar_y_convertir(cadena):
    # Reemplazamos . y - por comas para unificar
    regex = r"[a-zA-Z]+"

    cadena = cadena.replace('.', ',').replace('-', ',')
    cadena = re.sub(regex, ',',cadena)
    # Dividimos por comas y convertimos a enteros
    return {int(num) for num in cadena.split(',') if num.strip().isdigit()}

def normalizar_lista(cadena):
    # Reemplazamos . y - por comas para unificar
    regex = r"[a-zA-Z]+"

    cadena = cadena.replace('.', ',').replace('-', ',')
    cadena = re.sub(regex, ',',cadena)
    # Dividimos por comas y convertimos a enteros
    return [int(num) for num in cadena.split(',') if num.strip().isdigit()]
