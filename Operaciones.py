def registrar_expediente():
    """Solicita, valida y almacena los datos de un nuevo expediente."""
    config.mostrar_titulo("REGISTRAR NUEVO EXPEDIENTE")

    # Generar código correlativo automático (EXP-001, EXP-002, etc.)
    nuevo_codigo = f"EXP-{len(config.codigos) + 1:03d}"
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

    tipo_doc = elegir_tipo_documento()
    asunto = solicitar_texto("Ingrese el asunto del trámite: ")
    descripcion = solicitar_texto("Ingrese la descripción detallada: ")

    # Almacenar en las listas globales del módulo config
    config.codigos.append(nuevo_codigo)
    config.dnis.append(dni)
    config.nombres.append(nombres_ingresados)
    config.apellidos.append(apellidos_ingresados)
    config.correos.append(correo)
    config.telefonos.append(tel)
    config.tipos_documento.append(tipo_doc)
    config.asuntos.append(asunto)
    config.descripciones.append(descripcion)

    print(f"\n¡Éxito! Expediente {nuevo_codigo} registrado correctamente.")


def listar_expedientes():
    """Muestra todos los expedientes registrados."""
    config.mostrar_titulo("LISTADO DE EXPEDIENTES")

    if not config.codigos:
        print("No hay expedientes registrados en el sistema.")
        return

    for i in range(len(config.codigos)):
        print(f"Expediente N° {i + 1} - Código: {config.codigos[i]}")
        print(f"  Ciudadano: {config.nombres[i]} {config.apellidos[i]}")
        print(
            f"  Identificación: {config.dnis[i]} | Tipo de Documento: {config.tipos_documento[i]}"
        )
        print(f"  Contacto: Tel: {config.telefonos[i]} | Correo: {config.correos[i]}")
        print(f"  Asunto: {config.asuntos[i]}")
        print(f"  Descripción: {config.descripciones[i]}")
        print("-" * 50)