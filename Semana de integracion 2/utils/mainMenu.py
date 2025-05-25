from utils.menu import menu, sub_menu_conjuntos, sub_menu_producto_cartesiano
from utils.graficoVennDiferencia import mostrar_venn_con_elementos
from utils.graficosVenn import diferencia_entre_dos, union_varios, interseccion_varios, diferencia_simetrica_y_diferencias
from utils.operaciones import contar_frecuencia, sumar_digitos, digitos_compartidos, diversidad_alta
from utils.normalizador import limpiar_y_convertir
from utils.menu import menu, sub_menu_conjuntos, sub_menu_producto_cartesiano

OPCION_NO_VALIDA = "Opción no válida. Intente nuevamente."


P = {0, 1, 2, 3, 4, 5, 9}
R = {2, 3, 4, 8, 9}
E = {3, 4, 5, 6, 7, 8}
conjuntos = []

def main_loop():
    main_menu = True
    while main_menu:
        opcion = menu()
        
        if opcion == "1":
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
            '''pedir al usuario que ingrese dos conjuntos y mostrar la diferencia entre ellos'''
            '''print la diferencia. y dejar una opcion que diga, si quiere ver el grafico.'''
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
            # Lógica para producto cartesiano
            pass
        elif sub_option == "2":
            # Lógica para producto cartesiano con repetición
            pass
        elif sub_option == "3":
            break
        else:
            print(OPCION_NO_VALIDA)
