def generar_codigo_expediente(codigos):
    numero = len(codigos) + 1
    return f"EXP-{numero:03d}"
