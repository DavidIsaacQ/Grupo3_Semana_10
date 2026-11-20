def solicitar_dni():
    while True:
        dni = input("Ingrese DNI (8 dígitos): ").strip()
        if len(dni) == 8 and dni.isdigit():
            return dni
        print("[!] Error: El DNI debe tener exactamente 8 dígitos numéricos.")

