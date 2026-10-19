codigos = []
dnis = []
nombres = []
apellidos = []
correos = []
telefonos = []
tipos_documento = []
asuntos = []
descripciones = []

# Opciones fijas para el tipo de documento
TIPOS_DOCUMENTO = ["DNI", "Carnet de Extranjería", "Pasaporte", "RUC"]

# Constantes del menú
OPCION_REGISTRAR = 1
OPCION_LISTAR = 2
OPCION_SALIR = 3


def mostrar_titulo(texto):
    """Genera un encabezado visual estandarizado."""
    print()
    print("=" * 50)
    print(texto.center(50))
    print("=" * 50)


def mostrar_menu():
    """Muestra el menú de opciones en la consola."""
    mostrar_titulo("MESA DE PARTES DIGITAL")
    print(f"    {OPCION_REGISTRAR}. Registrar expediente")
    print(f"    {OPCION_LISTAR}. Listar expedientes")
    print(f"    {OPCION_SALIR}. Salir")
    print("-" * 50)