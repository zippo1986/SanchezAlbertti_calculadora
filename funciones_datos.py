def imprimir_mensaje(mensaje):
    print(mensaje)
    
def ingresar_dato(mensaje):
    dato = input(mensaje)
    
    return dato
def mostrar_resultados(diccionario_operaciones):
    imprimir_mensaje("Menu de resultados ")
    imprimir_mensaje(f"El resultado de A+B = {diccionario_operaciones["suma"]}")
    imprimir_mensaje(f"El resultado de A-B= {diccionario_operaciones["resta"]}")
    imprimir_mensaje(f"El resultado de A*B= {diccionario_operaciones["multiplicacion"]}")
    imprimir_mensaje(f"El resultado de A/B= {diccionario_operaciones["division"]}")
    imprimir_mensaje(f"El resultado de !A = {diccionario_operaciones["factorial uno"]}")
    imprimir_mensaje(f"El resultado de !B = {diccionario_operaciones["factorial dos"]}")