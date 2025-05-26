from utils.graficoVennDiferencia import mostrar_venn_con_elementos
from utils.graficosVenn import diferencia_entre_dos, union_varios, interseccion_varios, diferencia_simetrica_y_diferencias
from utils.operaciones import contar_frecuencia, sumar_digitos, digitos_compartidos, diversidad_alta
from utils.normalizador import limpiar_y_convertir
from utils.menu import menu, sub_menu_conjuntos, sub_menu_producto_cartesiano
from utils.mainMenu import main_loop


'''
mostrar_venn_con_elementos(P, R)

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

'''
test = input('Ingrese un conjunto de números separados por comas: ')
conjunto = limpiar_y_convertir(test)
conjuntos = []
P = {0, 1, 2, 3, 4, 5, 9}
R = {3,4,2,9,2,2,8,2}
E = {3, 4, 5, 6, 7, 8}



print(f'Conjunto ingresado: {conjunto}')

conjuntos.append(P)
conjuntos.append(R)
conjuntos.append(E)

print(f'Conjuntos: {conjuntos}')
'''

'''print(f'Frecuencia de los elementos en el conjunto: {contar_frecuencia(R)}')
print(f'Suma de los elementos del conjunto: {sumar_digitos(R)}')
print(f'Dígitos compartidos entre los conjuntos: {digitos_compartidos(conjuntos)}')
print(f'Conjuntos con alta diversidad (más de 6 elementos): {diversidad_alta(conjuntos)}')MAL ELIMINA LOS VALORES REPETIDOS, PORQUE ES UN SET, UTILIZAR LISTA []'''


'''
PARTE: HUGO

# Verificamos si todos los integrantes nacieron después del año 2000
# Usamos la función all() que devuelve True solo si todos cumplen la condición

if all(year > 2000 for year in years_nacimiento):
    print("\nGrupo Z")

"/////////////////////////////////////////////////////////////////////////////////////////////////////////"


# Ingresamos cuántos integrantes tenemos en el grupo
cantidad = int(input("¿Cuántos integrantes hay en el grupo? "))

# Creamos una lista para guardar los años de nacimiento
years_nacimiento = []

# Usamos un ciclo for para pedir el año de nacimiento de cada integrante
for i in range(cantidad):
    year = int(input(f"Ingresá el año de nacimiento del integrante {i+1}: "))
    years_nacimiento.append(year)  # Agregamos el año a la lista

# Pedimos el año actual para poder calcular las edades
year_actual = int(input("Ingresá el año actual: "))

# Calculamos las edades restando el año de nacimiento al año actual
edades = [year_actual - year for year in years_nacimiento]

# Mostramos las edades calculadas
print("\nEdades actuales de los integrantes:")
for i in range(len(edades)):
    print(f"Integrante {i+1}: {edades[i]} años")

# Ahora vamos a calcular el producto cartesiano entre los años y las edades
# significa que vamos a combinar cada año con cada edad posible
producto_cartesiano = []

# Doble ciclo para combinar cada año con cada edad
for year in years_nacimiento:
    for edad in edades:
        producto_cartesiano.append((year, edad))  # Agregamos la pareja (año, edad)

# Mostramos el producto cartesiano resultante
print("\nProducto cartesiano entre años de nacimiento y edades:")
for par in producto_cartesiano:
    print(par)  # Mostramos cada combinación


FIN PARTE HUGO
'''


if __name__ == "__main__":
    main_loop()
#     main_menu()