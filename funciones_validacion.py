def validar_numero(dato):
    try:
        float(dato)
        return True
    except ValueError:
        print("no es un valor válido")
        return False
    
