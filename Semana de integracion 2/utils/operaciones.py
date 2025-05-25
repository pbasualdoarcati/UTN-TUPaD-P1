def contar_frecuencia(conjunto):
    """Recibe un conjunto (o lista) y devuelve un diccionario con la frecuencia de cada dígito."""
    frecuencia = {}
    for digito in conjunto:
        frecuencia[digito] = frecuencia.get(digito, 0) + 1
    return frecuencia

def sumar_digitos(conjunto):
    """Recibe un conjunto (o lista) y devuelve la suma de sus dígitos."""
    suma = 0
    for digito in conjunto:
        suma += digito
    return suma

def digitos_compartidos(conjuntos):
    """Recibe una lista de conjuntos y devuelve el conjunto de dígitos que están en todos ellos."""
    if not conjuntos:
        return set()
    interseccion = conjuntos[0]
    for conjunto in conjuntos[1:]:
        interseccion = interseccion.intersection(conjunto)
    return interseccion

def diversidad_alta(conjuntos, umbral=6):
    """Recibe una lista de conjuntos y retorna una lista con los índices de los conjuntos que tengan más de 'umbral' elementos."""
    indices = []
    for i, conjunto in enumerate(conjuntos):
        if len(conjunto) > umbral:
            indices.append(i)
    return indices