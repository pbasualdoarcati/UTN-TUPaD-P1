from utils.graficoVennDiferencia import mostrar_venn_con_elementos
from utils.graficosVenn import diferencia_entre_dos, union_varios, interseccion_varios, diferencia_simetrica_y_diferencias
from utils.operaciones import contar_frecuencia, sumar_digitos, digitos_compartidos, diversidad_alta
from utils.normalizador import limpiar_y_convertir
from utils.menu import menu, sub_menu_conjuntos, sub_menu_producto_cartesiano
from utils.mainMenu import main_loop


'''
mostrar_venn_con_elementos(P, R)
Esto es una prueba

diferencia_entre_dos(P, R)
union_varios([P, R])
interseccion_varios([P, R])
diferencia_simetrica_y_diferencias(P, E)
diferencia = P - R
interseccion = P & R
diferenciaSimetrica = P ^ R
union = P | R
print(f'Unión entre P y R: {union}')
print(f'Unión entre P y R: {P.union(R)}')

print(f'Diferencia entre P y R: {diferencia}')
print(f'Diferencia entre P y R: {P.difference(R)}')

print(f'Intersección entre P y R: {interseccion}')
print(f'Intersección entre P y R: {P.intersection(R)}')

print(f'Diferencia entre P y R: {diferenciaSimetrica}')
print(f'Diferencia entre P y R: {P.symmetric_difference(R)}')

'''

'''if (not test) or (test == ''):
    test = '1,2,3,4,5,6,7,8,9'
    print(f'No ingresó un conjunto válido. Usando el conjunto por defecto: {test}')
    

'''

''' test = input('Ingrese un conjunto de números separados por comas: ')

test = limpiar_y_convertir(test)
print(f'Conjunto normalizado: {test}')

'''

''' conjunto = limpiar_y_convertir(test)
print(f'Conjunto ingresado: {conjunto}')
conjuntos.append(conjunto)
conjuntos.append(P)
conjuntos.append(R)
conjuntos.append(E)
print(f'Conjuntos: {conjuntos}')
print(f'Frecuencia de los elementos en el conjunto: {contar_frecuencia(conjunto)}')
print(f'Suma de los elementos del conjunto: {sumar_digitos(conjunto)}')
print(f'Dígitos compartidos entre los conjuntos: {digitos_compartidos(conjuntos)}')
print(f'Conjuntos con alta diversidad (más de 6 elementos): {diversidad_alta(conjuntos)}')

'''

if __name__ == "__main__":
    main_loop()
#     main_menu()