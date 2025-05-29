def pedirAnios():
    #Pido los años de nacimiento, si el usuario ingresa '0' sale del bucle y devuelve una lista con todos los años ingresados
    listaAnios=[]
    while True:
        anio=int(input("Ingrese el año de nacimiento o Ingrese '0' para continuar: "))
        if anio==0:
            break
        elif anio>2025:
            print("El año no es valido")
        else:
            listaAnios.append(anio)
    print("Continuando con el programa...")
    return listaAnios

def contarPares(listaAnios):
    #cuenta cuantos numeros pares hay en una lista
    pares=0
    for i in listaAnios:
        if i%2==0:
            pares+=1
    return pares

def contarImpares(listaAnios):
    #cuenta cuantos numeros impares hay en una lista
    impares=0
    for i in listaAnios:
        if i%2!=0:
            impares+=1
    return impares