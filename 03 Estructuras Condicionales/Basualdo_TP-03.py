from statistics import mode, median, mean
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
    if nota >= 6:
        print('Aprobado')
    elif nota > 10:
        print('Error: La nota ingresada no es válida. Debe estar entre 0 y 10.')
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
    
## Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
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
    
## Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.
password = input('Ingrese su contraseña: ')
if password.__len__() >= 8 and password.__len__() <= 14:
    print('Ha ingresado una contraseña correcta')
else:
    print('Por favor, ingrese una contraseña de entre 8 y 14 caracteres.')
    
## Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

numeros_aleatorios = [random.randint(1, 100) for i in range(10)]
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

    