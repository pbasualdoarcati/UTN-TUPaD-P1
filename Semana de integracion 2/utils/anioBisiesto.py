from datetime import datetime

# Constante para mostrar cuando el usuario ingresa un dato incorrecto
OPCION_NO_VALIDA = "Opción no válida. Intente nuevamente."

def es_bisiesto(anio: int) -> bool:
    # Determina si un año es bisiesto.
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def obtener_edad(anio_nacimiento: int) -> int:
    # Calcula la edad actual según el año de nacimiento.
    return datetime.now().year - anio_nacimiento

def ingresar_anio(integrante_num: int) -> int:
    
    # Solicita el año de nacimiento de un integrante.
    # Valida que sea un número entero entre 1900 y el año actual.
    
    anio_actual = datetime.now().year

    while True:
        entrada = input(f"Ingresá el año de nacimiento del integrante {integrante_num}: ").strip()

        if not entrada.isdigit():
            print(OPCION_NO_VALIDA)
            continue

        anio = int(entrada)

        if 1900 <= anio <= anio_actual:
            return anio
        else:
            print(OPCION_NO_VALIDA)

def anio_bisiesto(integrantes: int = 5) -> None:
    # Controla el ingreso, validación, y análisis de años bisiestos de un grupo.
    anios_nacimiento = []

    print("\n-- Ingreso de años de nacimiento --\n")

    for i in range(1, integrantes + 1):
        anio = ingresar_anio(i)
        anios_nacimiento.append(anio)

    # Filtrar los años bisiestos ingresados
    anios_bisiestos = [anio for anio in anios_nacimiento if es_bisiesto(anio)]

    # Mostrar si hay o no años especiales
    if anios_bisiestos:
        print(f"\nTenemos un año especial. Años bisiestos: {', '.join(map(str, anios_bisiestos))}")
    else:
        print("\nNingún integrante nació en un año bisiesto.")

    # Mostrar edades actuales
    print("\n-- Edades actuales --\n")
    for i, anio in enumerate(anios_nacimiento, start=1):
        edad = obtener_edad(anio)
        print(f"Integrante {i}: {edad} años")