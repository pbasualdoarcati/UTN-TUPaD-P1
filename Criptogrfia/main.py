# main.py
from simulacion_comunicacion import SimulacionComunicacion

def menu():
    print("\n--- Simulación de Comunicación Segura con RSA ---")
    print("1. Enviar mensaje de A a B")
    print("2. Enviar mensaje de B a A")
    print("3. Salir")

def ejecutar_simulacion():
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
