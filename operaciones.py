
def listar_expedientes(codigos, dnis, nombres, apellidos,
correos, telefonos, asuntos, descripciones):
    print("\n--- LISTADO GENERAL DE EXPEDIENTES ---")
    
    if len(codigos) == 0:
        print("[i] Aún no hay expedientes registrados en el sistema.")
        return
