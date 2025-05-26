import math

## 1) Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal
def imprimir_hola_mundo():
    print("Hola Mundo!")
    
## 2) Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))

## 3) Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

## 4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio
radio = float(input("Ingrese el radio del círculo: "))
print(f"El área del círculo es: {calcular_area_circulo(radio)} y el perímetro es: {calcular_perimetro_circulo(radio)}")

## 5) Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return f"{horas} horas, {minutos} minutos y {segundos_restantes} segundos"
segundos = int(input("Ingrese la cantidad de segundos: "))
print(f"{segundos} segundos son: {segundos_a_horas(segundos)}")

## 6) Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función. 

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

## 7) Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "Error: División por cero"
    return (suma, resta, multiplicacion, division)  
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
resultados = operaciones_basicas(a, b)
print(f"Resultados:\nSuma: {resultados[0]}\nResta: {resultados[1]}\nMultiplicación: {resultados[2]}\nDivisión: {resultados[3]}") 

## 8) Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
print(f"Su IMC es: {calcular_imc(peso, altura)}")

## 9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 2)
celsius = float(input("Ingrese la temperatura en Celsius: "))
print(f"{celsius}°C son {celsius_a_fahrenheit(celsius)}°F")

## 10) Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return round(promedio, 2)
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
print(f"El promedio de los números es: {calcular_promedio(a, b, c)}")
