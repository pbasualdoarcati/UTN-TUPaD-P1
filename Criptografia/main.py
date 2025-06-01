# main.py
from simulacion_comunicacion import SimulacionComunicacion
from pathlib import Path
from generar_claves import generar_y_guardar_claves

def menu():
    print("\n--- Simulación de Comunicación Segura con RSA ---")
    print("1. Enviar mensaje de A a B")
    print("2. Enviar mensaje de B a A")
    print("3. Salir")
    
def verificar_y_generar_claves():
    carpeta_actual = Path(__file__).parent
    archivos_necesarios = [
        carpeta_actual / "user_a_private_key.pem",
        carpeta_actual / "user_a_public_key.pem",
        carpeta_actual / "user_b_private_key.pem",
        carpeta_actual / "user_b_public_key.pem",
    ]
    
    # Si falta algún archivo, generar claves nuevas
    if not all(f.exists() for f in archivos_necesarios):
        print("Claves no encontradas. Generando nuevas claves para usuarios A y B...")
        generar_y_guardar_claves("user_a")
        generar_y_guardar_claves("user_b")
    else:
        print("Claves encontradas. Continuando...")

def ejecutar_simulacion():
    verificar_y_generar_claves()
    simulador = SimulacionComunicacion()

    while True:
        menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            mensaje = input("Escribí el mensaje para B: ")
            cifrado = simulador.enviar_mensaje("A", "B", mensaje)
            print(f"\n📤 Mensaje cifrado: {cifrado}")
            descifrado = simulador.recibir_mensaje("B", cifrado)
            print(f"📥 B recibió: {descifrado}")
        
        elif opcion == "2":
            mensaje = input("Escribí el mensaje para A: ")
            cifrado = simulador.enviar_mensaje("B", "A", mensaje)
            print(f"\n📤 Mensaje cifrado: {cifrado}")
            descifrado = simulador.recibir_mensaje("A", cifrado)
            print(f"📥 A recibió: {descifrado}")

        elif opcion == "3":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Probá de nuevo.")

if __name__ == "__main__":
    ejecutar_simulacion()
