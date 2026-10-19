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

def solicitar_texto(mensaje):
    """Solicita un texto obligatorio y valida que no esté vacío."""
    while True:
        texto = input(mensaje).strip()
        if not texto:
            print("Error: Este campo no puede quedar vacío.")
        else:
            return texto


def validar_dni(dni):
    """Valida que el DNI tenga exactamente 8 dígitos numéricos."""
    if len(dni) != 8:
        return False
    for c in dni:
        if not c.isdigit():
            return False
    return True


def validar_telefono(tel):
    """Valida que el teléfono tenga exactamente 9 dígitos numéricos."""
    if len(tel) != 9:
        return False
    for c in tel:
        if not c.isdigit():
            return False
    return True


def elegir_tipo_documento():
    """Muestra los tipos de documento numerados y retorna el elegido."""
    print("\n--- SELECCIÓN DE DOCUMENTO ---")
    print("Seleccione la categoría o tipo de documento del ciudadano:")
    for posicion in range(len(TIPOS_DOCUMENTO)):
        print(f"   {posicion + 1}. {TIPOS_DOCUMENTO[posicion]}")

    while True:
        entrada = input("Seleccione el número de la opción: ").strip()
        if entrada.isdigit():
            numero = int(entrada)
            if 1 <= numero <= len(TIPOS_DOCUMENTO):
                return TIPOS_DOCUMENTO[numero - 1]
        print(
            f"Error: Ingrese un número válido entre 1 y {len(TIPOS_DOCUMENTO)}.")
