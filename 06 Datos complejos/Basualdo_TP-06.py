##  Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
## Añadir las siguientes frutas con sus respectivos precios:
##  Naranja = 1200
##  Manzana = 1500
##  Pera = 2300

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

## Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
## Banana = 1330
## Manzana = 1700
## Melón = 2800
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

## Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
frutas = list(precios_frutas.keys())

## Escribí un programa que permita almacenar y consultar números telefónicos.
## Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
## Luego, pedí un nombre y mostrale el número asociado, si existe.
contactos = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono: ")
    contactos[nombre] = numero
nombre_consulta = input("Ingrese el nombre del contacto a consultar: ")
if nombre_consulta in contactos:
    print(f"El número de {nombre_consulta} es: {contactos[nombre_consulta]}")
else:
    print(f"No se encontró el contacto {nombre_consulta}.")

## 5) Solicita al usuario una frase e imprime:
## Las palabras únicas (usando un set).
## Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

contador_palabras = {}
for palabra in palabras:
    contador_palabras[palabra] = contador_palabras.get(palabra, 0) + 1
print("Cantidad de veces que aparece cada palabra:", contador_palabras)

## 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
## Luego, mostrá el promedio de cada alumno.

alumnos = {}
for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = tuple(float(input(f"Ingrese la nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio}")
    
## Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
## Mostrá los que aprobaron ambos parciales.
## Mostrá los que aprobaron solo uno de los dos.
## Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
parcial_1 = {101, 102, 103, 104}
parcial_2 = {103, 104, 105, 106}
aprobados_ambos = parcial_1.intersection(parcial_2)
aprobados_uno = parcial_1.symmetric_difference(parcial_2)
aprobados_total = parcial_1.union(parcial_2)
print("Aprobados en ambos parciales:", aprobados_ambos)
print("Aprobados en solo uno de los dos parciales:", aprobados_uno)
print("Aprobados en al menos un parcial:", aprobados_total)

## 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
## Consultar el stock de un producto ingresado.
## Agregar unidades al stock si el producto ya existe.
## Agregar un nuevo producto si no existe.

productos_stock = {}
def consultar_stock(producto):
    return productos_stock.get(producto, "Producto no encontrado.")
def agregar_stock(producto, unidades):
    if producto in productos_stock:
        productos_stock[producto] += unidades
    else:
        productos_stock[producto] = unidades
def agregar_producto(producto, unidades):
    if producto not in productos_stock:
        productos_stock[producto] = unidades
    else:
        print("El producto ya existe. Use agregar_stock para aumentar el stock.")
while True:
    accion = input("Ingrese 'consultar', 'agregar stock' o 'agregar producto' (o 'salir' para terminar): ").strip().lower()
    if accion == 'salir':
        break
    elif accion == 'consultar':
        producto = input("Ingrese el nombre del producto a consultar: ")
        print(consultar_stock(producto))
    elif accion == 'agregar stock':
        producto = input("Ingrese el nombre del producto: ")
        unidades = int(input("Ingrese la cantidad de unidades a agregar: "))
        agregar_stock(producto, unidades)
        print(f"Stock actualizado: {productos_stock[producto]}")
    elif accion == 'agregar producto':
        producto = input("Ingrese el nombre del nuevo producto: ")
        unidades = int(input("Ingrese la cantidad de unidades: "))
        agregar_producto(producto, unidades)
        print(f"Producto agregado: {producto} con stock {productos_stock[producto]}")
    else:
        print("Ingrese una opcion correcta. Intente nuevamente.")
    
## ) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
agenda = {}
def agregar_evento(dia, hora, evento):
    agenda[(dia, hora)] = evento
def consultar_evento(dia, hora):
    return agenda.get((dia, hora), "No hay evento programado para este día y hora.")
while True:
    accion = input("Ingrese 'agregar' para agregar un evento, 'consultar' para consultar un evento o 'salir' para terminar: ").strip().lower()
    if accion == 'salir':
        break
    elif accion == 'agregar':
        dia = input("Ingrese el día del evento (formato DD/MM): ")
        hora = input("Ingrese la hora del evento (formato HH:MM): ")
        evento = input("Ingrese el nombre del evento: ")
        agregar_evento(dia, hora, evento)
        print(f"Evento agregado: {evento} en {dia} a las {hora}.")
    elif accion == 'consultar':
        dia = input("Ingrese el día del evento a consultar (formato DD/MM): ")
        hora = input("Ingrese la hora del evento a consultar (formato HH:MM): ")
        print(consultar_evento(dia, hora))
    else:
        print("Ingrese una opción correcta. Intente nuevamente.")   
        
## Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
## Las capitales sean las claves.
## Los países sean los valores
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Colombia': 'Bogotá'
}
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print("Diccionario de capitales y países:", capitales_paises)
