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


