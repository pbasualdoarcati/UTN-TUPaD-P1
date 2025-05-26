
SELECCIONE_OPCION_PROMPT = "Seleccione una opción: "

def menu ():
    print("1. Trabajar con conjuntos")
    print("2. Trabajar con producto cartesiano")
    print("3. Salir")
    opcion = input(SELECCIONE_OPCION_PROMPT)
    return opcion

def sub_menu_conjuntos():
    print("1. Mostrar Venn con elementos")
    print("2. Diferencia entre dos conjuntos")
    print("3. Unión de dos conjuntos")
    print("4. Intersección de dos conjuntos")
    print("5. Diferencia simétrica de dos conjuntos")
    print("6. Volver")
    opcion = input(SELECCIONE_OPCION_PROMPT)
    return opcion


def sub_menu_producto_cartesiano():
    print("1. Producto cartesiano")
    print("2. Producto cartesiano con repetición")
    print("3. Volver")
    print("4. Calcular grupo Z")
    print("5. Calcular producto cartesiano")
    opcion = input(SELECCIONE_OPCION_PROMPT)
    return opcion

