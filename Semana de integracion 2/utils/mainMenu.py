from utils.menu import menu, sub_menu_conjuntos, sub_menu_producto_cartesiano
from utils.graficoVennDiferencia import mostrar_venn_con_elementos
from utils.graficosVenn import diferencia_entre_dos, union_varios, interseccion_varios, diferencia_simetrica_y_diferencias
from utils.operaciones import contar_frecuencia, sumar_digitos, digitos_compartidos, diversidad_alta
from utils.normalizador import limpiar_y_convertir
from utils.productoCartesiano import producto_cartesiano
from utils.anioBisiesto import anio_bisiesto

OPCION_NO_VALIDA = "Opción no válida. Intente nuevamente."

mock = [1990,2001, 2002, 2003]
P = {0, 1, 2, 3, 4, 5, 9}
R = {2, 3, 4, 8, 9}
E = {3, 4, 5, 6, 7, 8}
conjuntos = []

def main_loop():
    main_menu = True
    while main_menu:
        opcion = menu()
        
        if opcion == "1":
            '''una función que le solicite al usuario ingresar la cantidad de integrantes que desea trabajar, y luego le solicite los DNI
            en base a ese FOR vas a sacar 2 variables, una que sea de tipo set, y otra que sea de tipo list. 
            La set, va a pasar por el normlizador limpiar_y_convertir porque devuelve un conjunto de numeros enteros, y la lista tiene que pasar por otro normalizador pero que devuelva una lista de numeros enteros
            Mostrar un menu, que diga, que quiere hacer con esos conjuntos? Si quiere union, intersección, diferencia o diferencia simétrica.
            Union, cantidad de sets: Ej:
            [
                {0, 1, 2, 3, 4, 5, 9},
                {2, 3, 4, 8, 9},
                {3, 4, 5, 6, 7, 8}
            ]
            setters = []
            listasDni = []
            for i in range(cantidad_integrantes):
                dni = input(f"Ingrese el DNI del integrante {i + 1}: ")
                conjunto_set = limpiar_y_convertir(dni)
                conjunto_list = normalizar_lista(dni)
                setters.append(conjunto_set)
                listasDni.append(conjunto_list)
            
            menu, opciones = {
                "1": "Unión de conjuntos",
                "2": "Intersección de conjuntos",
                "3": "Diferencia de conjuntos",
                "4": "Diferencia simétrica de conjuntos",
                "5": "Salir"
            }
            si selecciona 1:
            
            def union_varios(conjuntos):
            unionConjuntos = set()
            for i in range(len(conjuntos) - 1):
                unionConjuntos = conjuntos[i].union(conjuntos[i + 1])
            return print(f"Unión de conjuntos: {unionConjuntos}")

            P.union(R).union(E)
            P.intersection(R).intersection(E)
            P.difference(R).difference(E)
            P.symmetric_difference(R).symmetric_difference(E)
            '''
            ejecutar_submenu_conjuntos()
        
        elif opcion == "2":
            ejecutar_submenu_producto_cartesiano()
        
        elif opcion == "3":
            print("Saliendo del programa...")
            main_menu = False
        
        else:
            print(OPCION_NO_VALIDA)


def ejecutar_submenu_conjuntos():
    while True:
        sub_option = sub_menu_conjuntos()
        if sub_option == "1":
            mostrar_venn_con_elementos(P, R)
        elif sub_option == "2":
            diferencia_entre_dos(P, R)
        elif sub_option == "3":
            union_varios([P, R])
        elif sub_option == "4":
            interseccion_varios([P, R])
        elif sub_option == "5":
            diferencia_simetrica_y_diferencias(P, E)
        elif sub_option == "6":
            break
        else:
            print(OPCION_NO_VALIDA)


def ejecutar_submenu_producto_cartesiano():
    while True:
        sub_option = sub_menu_producto_cartesiano()
        if sub_option == "1":
            integrantes  = int(input("Ingrese la cantidad de integrantes: "))
            # Lógica para producto cartesiano
            pass
        elif sub_option == "2":
            anio_bisiesto(mock)
        elif sub_option == "3":
            break
        elif sub_option == "4":
            producto_cartesiano(mock)
        else:
            print(OPCION_NO_VALIDA)
