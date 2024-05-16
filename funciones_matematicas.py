def sumar (num_uno: int, num_dos:int):
    
    return num_uno + num_dos
def restar (num_uno: int, num_dos:int):
    return num_uno - num_dos

def multiplicar(num_uno, num_dos):
    return num_uno * num_dos
def dividir(num_uno, num_dos):
    
    if num_dos == 0:
        raise ZeroDivisionError
        
    else:
        return num_uno/num_dos

def factorial(n):
    if n < 0:
        raise ValueError
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def calcular_operaciones (num_uno,num_dos,diccionario_operaciones):
    
    diccionario_operaciones["suma"] = sumar(num_uno,num_dos)
    diccionario_operaciones["resta"] = restar(num_uno,num_dos)
    diccionario_operaciones["multiplicacion"]= multiplicar(num_uno,num_dos)
    try:
        diccionario_operaciones["division"]= dividir(num_uno,num_dos)
    except ZeroDivisionError:
        diccionario_operaciones["division"] = "No se puede dividir por 0"
    try:
        diccionario_operaciones["factorial uno"] = factorial(num_uno)
        
    except ValueError:
        diccionario_operaciones["factorial uno"] = "No se puede hacer factorial de un numero negativo"
    try:
        diccionario_operaciones["factorial dos"] = factorial(num_uno)
        
    except ValueError:
        diccionario_operaciones["factorial dos"] = "No se puede hacer factorial de un numero negativo"
    
    
    