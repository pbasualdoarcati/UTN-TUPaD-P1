# AND | OR | NOT 
"""
Este script implementa un generador de tablas de verdad para las operaciones lógicas AND, OR y NOT.
Permite al usuario seleccionar la operación deseada e ingresar valores para su evaluación.
El script también muestra los colaboradores del proyecto al salir.
Funciones:
----------
mostrarIntegrantes():
    Imprime los nombres de los colaboradores del proyecto.
mostrarTabla(a, b, option, result):
    Muestra la tabla de verdad para la operación lógica seleccionada.
    Parámetros:
        a (int): El primer operando (0 o 1).
        b (int): El segundo operando (0 o 1). No se utiliza para la operación NOT.
        option (str): La operación seleccionada ("1" para AND, "2" para OR, "3" para NOT).
        result (int): El resultado de la operación lógica.
tablaVerdad():
    Función principal para interactuar con el usuario.
    Solicita al usuario seleccionar una operación lógica e ingresar valores.
    Se llama recursivamente para permitir múltiples evaluaciones hasta que el usuario decida salir.
Variables Globales:
-------------------
convert (dict):
    Un diccionario que mapea los enteros 1 y 0 a sus equivalentes booleanos True y False.
"""

convert = {
    1: True,
    0: False
}

print("#" + "-" * 46 + "#")
print("|{:^46}|".format("Trabajo Práctico Integrado"))
print("|{:^46}|".format("Grupo Tecno-Late"))
print("#" + "-" * 46 + "#")

def mostrarIntegrantes():
    print("\nEste trabajo fue realizado por:")
    print("- Dante Kaddarian")
    print("- Pablo Basualdo Arcati")
    print("- Hugo Agustin Albertini")
    print("- Elias Carulla")
    print("- Renzo Calcatelli")

def mostrarTabla (a, b, option, result):
    if option == "1":
        print(f" A | B | A AND B\n---|---|--------\n {a} | {b} |   {result}")
    elif option == "2":
        print(f" A | B | A OR B\n---|---|-------\n {a} | {b} |   {result}")
    else:
        print(f" A | NOT A\n---|------\n {a} |   {result}")

def tablaVerdad ():
    option = input("¿Que tabla de verdad deseas ver? \n1. AND \n2. OR \n3. NOT \n4. Salir \nOpcion: ")
    while option not in ["1", "2", "3", "4"]:
        option = input("Opcion no valida, intenta de nuevo: ")
    
    if option == "1":
        a = input("Ingresa el valor de A (0 o 1): ")
        while a not in ["0", "1"]:
            print("Valor invalido, solo se puede ingresar 0 o 1.")
            a = input("Ingresa el valor de A (0 o 1): ")                     
        b = input("Ingresa el valor de B (0 o 1): ")
        while b not in ["0", "1"]:
            print("Valor invalido, solo se puede ingresar 0 o 1.")
            b = input("Ingresa el valor de B (0 o 1): ")  
        a = int(a)
        b = int(b)
        result = 1 if convert[a] and convert[b] else 0
        mostrarTabla(a, b, option, result)
        tablaVerdad()
    
    elif option == "2":
        a = input("Ingresa el valor de A (0 o 1): ")
        while a not in ["0", "1"]:
            print("Valor invalido, solo se puede ingresar 0 o 1.")
            a = input("Ingresa el valor de A (0 o 1): ")                
        b = input("Ingresa el valor de B (0 o 1): ")
        while b not in ["0", "1"]:
            print("Valor invalido, solo se puede ingresar 0 o 1.")
            b = input("Ingresa el valor de B (0 o 1): ")  
        a = int(a)
        b = int(b)
        result = 1 if convert[a] or convert[b] else 0
        mostrarTabla(a, b, option, result)
        tablaVerdad()
    
    elif option == "3":
        a = input("Ingresa el valor de A (0 o 1): ")
        while a not in ["0", "1"]:
            print("Valor invalido, solo se puede ingresar 0 o 1.")
            a = input("Ingresa el valor de A (0 o 1): ")              
        a = int(a)
        result = 1 if not convert[a] else 0
        mostrarTabla(a, None, option, result)
        tablaVerdad()
    else:
        mostrarIntegrantes()
        return
    
tablaVerdad()

