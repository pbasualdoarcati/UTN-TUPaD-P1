def contar_frecuencia(numeros):
    """Recibe una lista de números y devuelve un diccionario con la frecuencia de cada número."""
    frecuencia = {}
    for numero in numeros:
        frecuencia[numero] = frecuencia.get(numero, 0) + 1
    return frecuencia

def sumar_digitos(numeros):
    """Recibe una lista de números y devuelve la suma de sus dígitos."""
    return sum(numeros)

def digitos_compartidos(numeros):
    """Recibe una lista de números y devuelve el conjunto de dígitos que están presentes en la lista."""
    return set(numeros)

def diversidad_alta(numeros, umbral=6):
    """Recibe una lista de números y retorna True si la cantidad de elementos distintos supera el umbral."""
    return len(set(numeros)) > umbral