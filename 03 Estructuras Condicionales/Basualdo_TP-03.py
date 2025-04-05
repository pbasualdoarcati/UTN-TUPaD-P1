from statistics import mode, median, mean
from datetime import date, datetime
import random

## 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
MAYOR_EDAD = 18
edad = input('Ingrese su edad: ')

if edad.isnumeric():
    edad = int(edad)
    if edad >= MAYOR_EDAD:
        print('Es mayor de edad')
    else:
        print('Es menor de edad')
    
else:
    print('Error: La edad ingresada no es un número válido.')
    
    
## 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = input('Ingrese su nota: ')
if nota.isnumeric():
    nota = float(nota)
    if nota > 10:
        print('Error: La nota ingresada no es válida. Debe estar entre 0 y 10.')
    elif nota >= 6:
        print('Aprobado')
    else:
        print('Desaprobado')
else:
    print('Error: La nota ingresada no es un número válido.')

## 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = input('Ingrese un número: ')
if numero.isnumeric():
    numero = float(numero)
    if numero % 2 == 0:
        print('El número es par')
    else:
        print('El número es impar')
else:
    print('Error: El número ingresado no es un número válido.')
    
## 4)Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
## Niño/a: menor de 12 años.
## Adolescente: mayor o igual que 12 años y menor que 18 años.
## Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
## Adulto/a: mayor o igual que 30 años.

BOY = 12
ADOLESCENTE = 18
ADULTO = 30

nuevaEdad = input('Ingrese su edad: ')
if nuevaEdad.isnumeric():
    nuevaEdad = int(nuevaEdad)
    if nuevaEdad < BOY:
        print('Es un niño')
    elif nuevaEdad >= BOY and nuevaEdad < ADOLESCENTE:
        print('Es un adolescente')
    elif nuevaEdad >= ADOLESCENTE and nuevaEdad < ADULTO:
        print('Es un adulto joven')
    elif nuevaEdad >= ADULTO:
        print('Es un adulto')
else:
    print('Error: La edad ingresada no es un número válido.')
    
## 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.
password = input('Ingrese su contraseña: ')
if password.__len__() >= 8 and password.__len__() <= 14:
    print('Ha ingresado una contraseña correcta')
else:
    print('Por favor, ingrese una contraseña de entre 8 y 14 caracteres.')
    
## 6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
print('Ejercicio 6')
numeros_aleatorios = [random.randint(1, 100) for i in range(10)]
print (f'Números aleatorios: {numeros_aleatorios}')
mode_num = mode(numeros_aleatorios)
median_num = median(numeros_aleatorios)
mean_num = mean(numeros_aleatorios)

print(f'Mediana: {median_num}')
print (f'Media: {mean_num}')

if mean_num > median_num and median_num > mode_num:
    print('Sesgo positivo')
elif mean_num < median_num and median_num < mode_num:
    print('Sesgo negativo')
elif mean_num == median_num and median_num == mode_num:
    print('No hay sesgo')

## 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla
frase = input('Ingrese una frase: ')
vowels = ['a', 'e', 'i', 'o', 'u']
frase = frase.lower()
lastLetter = frase[-1]
if frase.isalpha():
    if lastLetter in vowels:
        print(f'La frase termina en vocal: {lastLetter}')
    else:
        print(f'La frase termina en consonante: {lastLetter}')
else:
    print('Error: La frase ingresada no es válida. Debe contener solo letras.')
    
## 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
## Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
## Si quiere su nombre en minúsculas. Por ejemplo: pedro.
## Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.

options = {
    '1': str.upper,
    '2': str.lower,
    '3': str.title
}
newName = input('Ingrese su nombre: ')
print('Opciones de formato:')
print('1. Mayúscula')
print('2. Minúscula')
print('3. Capitalizar')
selection = input('Seleccione una opción: ')
if selection in options:
    formattedName = options[selection](newName)
    print(f'Nombre formateado: {formattedName}')
    
    
## 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla
MUY_LEVE = 3
LEVE = 4
MODERADO = 5
FUERTE = 6
MUY_FUERTE = 7

magnitud = input('Ingrese la magnitud del terremoto: ')
if magnitud.isnumeric():
    magnitud = float(magnitud)
    if magnitud < MUY_LEVE:
        print('Terremoto muy leve')
    elif magnitud >= MUY_LEVE and magnitud < LEVE:
        print('Terremoto leve')
    elif magnitud >= LEVE and magnitud < MODERADO:
        print('Terremoto Moderado')
    elif magnitud >= MODERADO and magnitud < FUERTE:
        print('Terremoto fuerte')
    elif magnitud >= FUERTE and magnitud < MUY_FUERTE:
        print('Terremoto muy fuerte')
    else:
        print('Terremoto devastador')
        
## 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano


fecha_str = input('Ingrese la fecha en formato aaaa-mm-dd: ')
fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
hemisferio = input('Ingrese el hemisferio (N/S): ').upper()
inicioInvierno = date(fecha.year, 12, 21)
inicioPrimavea = date(fecha.year, 3, 21)
inicioVerano = date(fecha.year, 6, 21)
inicioOtono = date(fecha.year, 9, 21)

if fecha >= inicioInvierno or fecha < inicioPrimavea:
    estacionNorte = 'Invierno'
elif fecha >= inicioPrimavea and fecha < inicioVerano:
    estacionNorte = 'Primavera'
elif fecha >= inicioVerano and fecha < inicioOtono:
    estacionNorte = 'Verano'
else:
    estacionNorte = 'Otoño'
    
if hemisferio == 'N':
    print(f'La estación es: {estacionNorte}')
elif hemisferio == 'S':
    estacionOpuesta = {
        'Invierno': 'Verano',
        'Primavera': 'Otoño',
        'Verano': 'Invierno',
        'Otoño': 'Primavera'
    }
    print(f'La estación es: {estacionOpuesta[estacionNorte]}')
else:
    print('Error: El hemisferio ingresado no es válido. Debe ser N o S.')
    
