def solicitar_dni():
    while True:
        dni = input("Ingrese DNI (8 dígitos): ").strip()
        if len(dni) == 8 and dni.isdigit():
            return dni
        print("[!] Error: El DNI debe tener exactamente 8 dígitos numéricos.")

def solicitar_telefono():
    while True:
        telefono = input("Ingrese Teléfono móvil (9 dígitos): ").strip()
        if len(telefono) == 9 and telefono.isdigit():
            return telefono
        print("[!] Error: El teléfono debe tener exactamente 9 dígitos numéricos.")

def solicitar_correo():
    while True:
        correo = input("Ingrese Correo electrónico: ").strip().lower()
        partes = correo.split("@")
        if len(partes) == 2 and len(partes[0]) > 0 and "." in partes [1] and " " not in correo:
            return correo
        print ("Error: Formato de correo invalido. ")

correo_valido = solicitar_correo()
print("Correo registrado correctamente:", correo_valido)

