from random import random
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
"""
for i in range (0, 101):
    print (f"{i}")
""" 
# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
"""
digito = int(input("Ingrese un dígito: "))
contador = 0
while digito > 0:
    digito = digito // 10
    contador += 1
print (f"La cantidad de dígitos es: {contador}")
"""
# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
"""
primerValor = int(input("Ingrese el primer valor: "))
segundoValor = int(input("Ingrese el segundo valor: "))
contadorEntreDosValores = 0
if(primerValor < 0 or segundoValor < 0):
    print("Los valores deben ser positivos")
else:
    if ( primerValor > segundoValor ):
        for i in range (segundoValor, primerValor):
                contadorEntreDosValores += 1
    else :
        for i in range (primerValor, segundoValor):
                contadorEntreDosValores += 1

print (f"La cantidad de números enteros entre {primerValor} y {segundoValor} es: {contadorEntreDosValores}")
"""
# 4)Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
"""
numero = int(input("Ingrese un número entero: "))
suma = 0
while numero != 0:
    suma += numero
    numero = int(input("Ingrese un número entero (0 para terminar): "))
print(f"La suma de los números ingresados es: {suma}")
"""
# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""
numeroAdivinanza = int(input("Ingrese un número entre 1 y 9: "))
numeroAleatorio = int(random()*10)
contadorIntentos = 0
while numeroAdivinanza != numeroAleatorio:
    if numeroAdivinanza < numeroAleatorio:
        print("El número es mayor")
    else:
        print("El número es menor")
    numeroAdivinanza = int(input("Ingrese un número entre 1 y 9: "))
    contadorIntentos += 1
print(f"¡Felicidades! Adivinaste el número {numeroAleatorio} en {contadorIntentos} intentos.")
"""
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente
"""
for i in range(102, 0, -2):
    print(i)
"""
# 7)  Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario
"""
numeroUsuario = int(input("Ingrese un número entero: "))
suma = 0
for i in range (0, numeroUsuario):
    suma += i
print (f"La suma de los números enteros desde 0 hasta {numeroUsuario} es: {suma}")
"""
# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""
arrayNumeros = []
for i in range (0, 100):
    numero = int(input("Ingrese un número entero: "))
    arrayNumeros.append(numero)
pares = 0
impares = 0
negativos = 0
positivos = 0
for i in range (0, 100):
    if arrayNumeros[i] % 2 == 0:
        pares += 1
    else:
        impares += 1
    if arrayNumeros[i] < 0:
        negativos += 1
    else:
        positivos += 1
print (f"La cantidad de números pares es: {pares}")
print (f"La cantidad de números impares es: {impares}")
print (f"La cantidad de números negativos es: {negativos}")
print (f"La cantidad de números positivos es: {positivos}")
"""
# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.
"""
valores = []
for i in range (0, 100):
    numero = int(input("Ingrese un número entero: "))
    valores.append(numero)
suma = 0
for i in range (0, 100):
    suma += valores[i]
media = suma / 100
print (f"La media de los números ingresados es: {media}")
"""
# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numeroRotar = int(input("Ingrese un número entero: "))
esNegativo = numeroRotar < 0
numeroRotar = abs(numeroRotar)
numeroInvertido = 0
while numeroRotar > 0:
    digito = numeroRotar % 10
    numeroInvertido = numeroInvertido * 10 + digito
    numeroRotar = numeroRotar // 10
if esNegativo:
    numeroInvertido = -numeroInvertido
print (f"El número invertido es: {numeroInvertido}")
