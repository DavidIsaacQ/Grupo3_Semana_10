codigos = []
dnis = []
nombres = []
apellidos = []
correos = []
telefonos = []
asuntos = []
descripciones = []

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


def registrar_expediente():
    """Solicita, valida y almacena los datos de un nuevo expediente."""
    mostrar_titulo("REGISTRAR NUEVO EXPEDIENTE")

    # Generar código correlativo automático (EXP-001, EXP-002, etc.)
    nuevo_codigo = f"EXP-{len(codigos) + 1:03d}"
    print(f"Código asignado: {nuevo_codigo}")

    # Validar DNI
    while True:
        dni = solicitar_texto("Ingrese el DNI (8 dígitos): ")
        if validar_dni(dni):
            break
        print("Error: El DNI debe contener exactamente 8 números.")

    nombres_ingresados = solicitar_texto("Ingrese los nombres: ")
    apellidos_ingresados = solicitar_texto("Ingrese los apellidos: ")
    correo = solicitar_texto("Ingrese el correo electrónico: ")

    # Validar teléfono
    while True:
        tel = solicitar_texto("Ingrese el teléfono (9 dígitos): ")
        if validar_telefono(tel):
            break
        print("Error: El teléfono debe contener exactamente 9 números.")

    # Flujo directo al trámite (sin la pregunta redundante)
    asunto = solicitar_texto("Ingrese el asunto del trámite: ")
    descripcion = solicitar_texto("Ingrese la descripción detallada: ")

    # Almacenar en las listas globales
    codigos.append(nuevo_codigo)
    dnis.append(dni)
    nombres.append(nombres_ingresados)
    apellidos.append(apellidos_ingresados)
    correos.append(correo)
    telefonos.append(tel)
    asuntos.append(asunto)
    descripciones.append(descripcion)

    print(f"\n¡Éxito! Expediente {nuevo_codigo} registrado correctamente.")


def listar_expedientes():
    """Muestra todos los expedientes registrados."""
    mostrar_titulo("LISTADO DE EXPEDIENTES")

    if not codigos:
        print("No hay expedientes registrados en el sistema.")
        return

    for i in range(len(codigos)):
        print(f"Expediente N° {i + 1} | Código: {codigos[i]}")
        print(f"  Ciudadano: {nombres[i]} {apellidos[i]}")
        print(f"  Identificación (DNI): {dnis[i]}")
        print(f"  Contacto: Tel: {telefonos[i]} | Correo: {correos[i]}")
        print(f"  Asunto: {asuntos[i]}")
        print(f"  Descripción: {descripciones[i]}")
        print("-" * 50)


def ejecutar_sistema():
    """Controla el flujo principal del programa mediante el menú."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción del menú: ").strip()

        if opcion == str(OPCION_REGISTRAR):
            registrar_expediente()
        elif opcion == str(OPCION_LISTAR):
            listar_expedientes()
        elif opcion == str(OPCION_SALIR):
            print("\nGracias por usar la Mesa de Partes Digital. ¡Hasta luego!")
            break
        else:
            print("Error: Opción no válida. Por favor, intente de nuevo.")


ejecutar_sistema()