from utils.menu import menu, sub_menu_conjuntos, sub_menu_producto_cartesiano
from utils.graficoVennDiferencia import mostrar_venn_con_elementos
from utils.graficosVenn import diferencia_entre_dos, union_varios, interseccion_varios, diferencia_simetrica_y_diferencias
from utils.operaciones import contar_frecuencia, sumar_digitos, digitos_compartidos, diversidad_alta
from utils.normalizador import convertir_a_lista_de_listas, generar_digitos_unicos, limpiar_y_convertir
from utils.productoCartesiano import producto_cartesiano
from utils.anioBisiesto import anio_bisiesto
from utils.ingresarCantIntegrantes import ingresar_cantidad_integrantes
from utils.ingresarDnis import ingresar_dnis

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
            cantidad_integrantes = ingresar_cantidad_integrantes()
            dnis_list = ingresar_dnis(cantidad_integrantes) 
            dnis_list_of_lists = convertir_a_lista_de_listas(dnis_list)
            dnis_list_of_sets = generar_digitos_unicos(dnis_list)
            print(f"Conjunto de DNI (set): {dnis_list_of_sets}")
            print(f"Lista de DNI (list): {dnis_list_of_lists}")
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
