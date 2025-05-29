## 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def mostrar_factoriales_hasta(n):
    for i in range(1, n + 1):
        print(f"El factorial de {i} es {factorial(i)}")
        
def main():
        numero = int(input("Ingrese un número entero positivo: "))
        if numero < 1:
            print("Por favor, ingrese un número mayor o igual a 1.")
            return
        mostrar_factoriales_hasta(numero)

if __name__ == "__main__":
    main()


## 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def mostrar_fibonacci_hasta(n):
    for i in range(n):
        print(f"Fibonacci en la posición {i} es {fibonacci(i)}")
        
def main_fibonacci():
        numero = int(input("Ingrese un número entero positivo para la serie de Fibonacci: "))
        if numero < 0:
            print("Por favor, ingrese un número mayor o igual a 0.")
            return
        mostrar_fibonacci_hasta(numero)

if __name__ == "__main__":
    main_fibonacci()
    
## 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente < 0:
        return 1 / potencia(base, -exponente)
    else:
        return base * potencia(base, exponente - 1)
    
def main_potencia():
        base = float(input("Ingrese la base: "))
        exponente = int(input("Ingrese el exponente (entero): "))
        resultado = potencia(base, exponente)
        print(f"{base} elevado a {exponente} es {resultado}")

if __name__ == "__main__":
    main_potencia()
    
## 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    
def main_decimal_a_binario():
        numero = int(input("Ingrese un número entero positivo en base decimal: "))
        if numero < 0:
            print("Por favor, ingrese un número mayor o igual a 0.")
            return
        resultado = decimal_a_binario(numero)
        print(f"La representación en binario de {numero} es {resultado}")
 
if __name__ == "__main__":
    main_decimal_a_binario()