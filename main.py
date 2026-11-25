# definir estructuras base de almacenamiento paralelo
codigos = []
dnis = []
nombres = []
apellidos = []
correos = []
telefonos = []
asuntos = []
descripciones = []


# configurar opciones principales del menu
OPCION_REGISTRAR = "1"
OPCION_BUSCAR = "2"
OPCION_LISTAR = "3"
OPCION_SALIR = "4"

# Vista del menú pricipal por consola
def mostrar_menu():
    print("\n" + "=" * 45)
    print("   MESA DE PARTES DIGITAL - MDSJL")
    print("=" * 45)
    print(f"  {OPCION_REGISTRAR}. Registrar nuevo expediente")
    print(f"  {OPCION_BUSCAR}. Buscar expediente por DNI")
    print(f"  {OPCION_LISTAR}. Listar expedientes (ordenados)")
    print(f"  {OPCION_SALIR}. Salir")
    print("-" * 45)

# Ciclo de navegación y control de opciones

def ejecutar_sistema():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == OPCION_REGISTRAR:
            print(">> Módulo de registro pendiente de conexión")
        elif opcion == OPCION_BUSCAR:
            print(">> Módulo de búsqueda pendiente de conexión")
        elif opcion == OPCION_LISTAR:
            print(">> Módulo de listado pendiente de conexión")
        elif opcion == OPCION_SALIR:
            print("Cerrando el sistema. ¡Hasta luego!")
            break
        else:
            print("[!] Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar_sistema()

