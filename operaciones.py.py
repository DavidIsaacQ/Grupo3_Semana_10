def generar_codigo_expediente(codigos):
    numero = len(codigos) + 1
    return f"EXP-{numero:03d}"

def registrar_expediente(codigos, dnis, nombres, apellidos, correos, telefonos, asuntos, descripciones):
    print("\n--- REGISTRO DE NUEVO EXPEDIENTE ---")
    codigo = generar_codigo_expediente(codigos)
    
    dni = input("Ingrese DNI (8 dígitos): ").strip()
    nombre = input("Ingrese Nombres: ").strip()
    apellido = input("Ingrese Apellidos: ").strip()
    correo = input("Ingrese Correo: ").strip()
    telefono = input("Ingrese Teléfono (9 dígitos): ").strip()
    asunto = input("Ingrese Asunto del trámite: ").strip()
    descripcion = input("Ingrese Descripción detallada: ").strip()

    codigos.append(codigo)
    dnis.append(dni)
    nombres.append(nombre)
    apellidos.append(apellido)
    correos.append(correo)
    telefonos.append(telefono)
    asuntos.append(asunto)
    descripciones.append(descripcion)

    print(f"\n[OK] Expediente registrado con éxito. Código asignado: {codigo}")

    

