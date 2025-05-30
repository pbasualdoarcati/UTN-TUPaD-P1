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

def convertir_a_lista_de_listas(dnis_list):
    dnis_list_normalizados = []
    for dni in dnis_list:
    # Convierte el DNI a string y luego a lista de enteros (manteniendo repeticiones y orden)
        digitos = [int(digito) for digito in str(dni)]
        dnis_list_normalizados.append(digitos)
    return dnis_list_normalizados

def generar_digitos_unicos(dnis: list):
    dnis_digitos_unicos = []
    for dni in dnis:
        # Convierte el DNI a string, luego a set de enteros para eliminar repeticiones
        digitos_unicos = {int(digito) for digito in str(dni)}
        dnis_digitos_unicos.append(digitos_unicos)
    return dnis_digitos_unicos

#print(generar_digitos_unicos([35459831, 24357864, 11564878]))
## Salida: [{1, 2, 3, 4}, {1, 2, 4, 5, 6}]