## 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

listaMultiple = list(range(4, 101, 4))
print(listaMultiple)

## 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.

listaVariada = [1, "UTN", 3.14, True, {1: "uno", 2: "dos"}]
print(listaVariada[-2])

## 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. 

listaVacia = []
listaPalabras = ["Python", "Test", "Mundo"]
for i in range(0, len(listaPalabras)):
    listaVacia.append(listaPalabras [i])
print(listaVacia)

## 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[len(animales) -1] = "oso"
print(animales)

## 5) Se define una lista de numeros enteros, la función max() devuelve el mayor de ellos para posteriormente eliminarlo con el método remove(). En conclusión, Este algoritmo permite eliminar el mayor número de una lista de números enteros.

## 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros

listaMultipleCinco = list(range(10, 31, 5))
print(listaMultipleCinco[:2])

## 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

listaAutos = ["sedan", "polo", "suran", "gol"]
listaAutos[1:3] = ["fiesta", "focus"]
print(listaAutos)

## 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.

listaDobles = []

for i in range(5, 20, 5):
    listaDobles.append(i * 2)
print(listaDobles)

## 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
##     a) Agregar "jugo" a la lista del tercer cliente usando append.
##     b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
##     c) Eliminar "pan" de la lista del primer cliente.
##     d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
if ("fideos" in compras[1] ):
    index = compras[1].index("fideos")
    compras[1][index] = "tallarines"
compras[0].remove("pan")
print(compras)

## 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
## Posición lista_anidada[0]: 15
## Posición lista_anidada[1]: True
## Posición lista_anidada[2][0]: 25.5
## Posición lista_anidada[2][1]: 57.9
## Posición lista_anidada[2][2]: 30.6
## Posición lista_anidada[3]: False
## Imprimir la lista resultante por pantalla.

listaAnidada = [
    [1], 
    [True], 
    [25.5, 57.9, 30.6],
    [False]
]

print(listaAnidada)
