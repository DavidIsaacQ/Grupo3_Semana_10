# Listas simuladas para probar TU código de ordenamiento de forma independiente
codigos = ["EXP-003", "EXP-001", "EXP-005", "EXP-002"]
dnis = ["12345678", "87654321", "11223344", "44332211"]
nombres = ["Juan", "Ana", "Carlos", "Maria"]
apellidos = ["Perez", "Gomez", "Ruiz", "Torres"]
correos = ["a@mail.com", "b@mail.com", "c@mail.com", "d@mail.com"]
telefonos = ["911111111", "922222222", "933333333", "944444444"]
asuntos = ["Licencia", "Queja", "Permiso", "Reclamo"]
descripciones = ["Desc 1", "Desc 2", "Desc 3", "Desc 4"]


def ordenar_expedientes_burbuja():
    """Tu código del Paso 1, Paso 2 o Paso 3."""
    total = len(codigos)
    if total <= 1:
        return

    for i in range(total - 1):
        for j in range(total - 1 - i):
            if codigos[j] > codigos[j + 1]:
                # Aquí irá tu lógica de intercambio
                pass


# Bloque temporal solo para probar que tu función ordena los datos de prueba
if __name__ == "__main__":
    print("Antes de ordenar:", codigos)
    ordenar_expedientes_burbuja()
    print("Despues de ordenar:", codigos)