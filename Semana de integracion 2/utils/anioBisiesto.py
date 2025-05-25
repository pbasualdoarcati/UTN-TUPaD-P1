from datetime import datetime

def es_bisiesto(anio: int) -> bool:
    
    # Función que determina si un año es bisiesto.
    # Un año es bisiesto si es divisible por 4 y no por 100,
    # salvo que sea divisible por 400.
    
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def obtener_edad(anio_nacimiento: int) -> int:
    
    # Calcula la edad actual restando el año de nacimiento
    # al año actual obtenido del sistema.
    
    anio_actual = datetime.now().year
    return anio_actual - anio_nacimiento

def ingresar_anio(integrante_num: int) -> int:
    
    # Solicita al usuario ingresar el año de nacimiento de un integrante.
    # Valida que sea un número entero dentro del rango válido
    # (1900 hasta el año actual).
    
    while True:
        entrada = input(f"Ingresá el año de nacimiento del integrante {integrante_num}: ")
        
        # Verifico que la entrada sea solo números
        if not entrada.isdigit():
            print("Por favor, ingresá solo números.")
            continue
        
        anio = int(entrada)
        
        # Verifico que el año esté en un rango lógico
        if 1900 <= anio <= datetime.now().year:
            return anio
        else:
            print(f"El año debe estar entre 1900 y {datetime.now().year}.")

def main():
    cantidad_integrantes = 5  # Cantidad fija de integrantes para el grupo
    anios_nacimiento = []     # Lista para guardar los años ingresados
    
    print("\n -- Ingresar año de nacimiento -- \n")
    
    # Se piden los años de nacimiento uno por uno
    for i in range(1, cantidad_integrantes + 1):
        anio = ingresar_anio(i)
        anios_nacimiento.append(anio)
    
    # Compruebo si hay algún año bisiesto entre los ingresados
    if any(es_bisiesto(anio) for anio in anios_nacimiento):
        print("\n Tenemos un año especial.")
    else:
        print("\n Ningún integrante nació en un año bisiesto.")
    
    # Calculo las edades de los integrantes y las muestro
    edades = [obtener_edad(anio) for anio in anios_nacimiento]
    print("\n -- Edades actuales de los integrantes --\n")
    for i, edad in enumerate(edades, start=1):
        print(f"Integrante {i}: {edad} años")


if __name__ == "__main__":
    main()





