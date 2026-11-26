
def listar_expedientes(codigos, dnis, nombres, apellidos, correos,
                       telefonos, asuntos, descripciones):
    print("\n--- LISTADO GENERAL DE EXPEDIENTES ---")
    if len(codigos) == 0:
        print("[i] Aún no hay expedientes registrados en el sistema.")
        return

    ordenar_expedientes_burbuja(codigos, dnis, nombres, apellidos, 
    correos, telefonos, asuntos, descripciones)
    


    for i in range(len(codigos)):
        print("=" * 45)
        print(f"[{codigos[i]}] - {asuntos[i]}")
        print(f"  Solicitante : {nombres[i]} {apellidos[i]} (DNI: {dnis[i]})")
        print(f"  Contacto    : {correos[i]} | Tel: {telefonos[i]}")
        print(f"  Detalle     : {descripciones[i]}")
    print("=" * 45)

ARCHIVO_DATOS = "expedientes.txt"

def guardar_expedientes(codigos, dnis, nombres, apellidos, correos, telefonos, asuntos, descripciones):
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
        for i in range(len(codigos)):
            linea = f"{codigos[i]}|{dnis[i]}|{nombres[i]}|{apellidos[i]}|{correos[i]}|{telefonos[i]}|{asuntos[i]}|{descripciones[i]}\n"
            archivo.write(linea)