from funciones_matematicas import *
from funciones_validacion import *
from funciones_datos import *
import os
def main ():
    flag_cargar_numero_uno= False
    flag_cargar_numero_dos= False
    
    flag_calcular_operaciones= False
    diccionario_operaciones = {}
    num_uno = 0
    num_dos = 0
    flag_confirmacion = True
    
    while flag_confirmacion:
        imprimir_mensaje("*"*100)
        imprimir_mensaje("""                            Bienvenido a Calculadora                  """)
        imprimir_mensaje("*"*100)
    
        imprimir_mensaje(f"""
                            {"*" *50}
                            {num_uno}
                            {num_dos}
                            {"*" *50}
                            1. Ingresar 1er operando
                            2. Ingresar 2do operando 
                            3. Calcular todas las operaciones
                            4. Informar resultados""")
        
        
        eleccion= ingresar_dato("Ingrese la opcion deseada")
        
        match eleccion:
            case "1":
                num_uno= ingresar_dato("Ingrese el primer numero")
                while not validar_numero(num_uno):
                    num_uno = ingresar_dato("Ingrese el primer numero")
                num_uno = float(num_uno)
                flag_cargar_numero_uno = True
            case "2":
                if flag_cargar_numero_uno:    
                    num_dos= ingresar_dato("Ingrese el segundo numero")
                    while not validar_numero(num_dos):
                        num_dos = ingresar_dato("Ingrese el segundo numero")
                    num_dos = float(num_dos)
                    flag_cargar_numero_dos =True
                else:
                    imprimir_mensaje("No se puede cargar el segundo numero sin haber cargado el primero")
            case "3":
                if flag_cargar_numero_uno and flag_cargar_numero_dos:
                    calcular_operaciones(num_uno,num_dos,diccionario_operaciones)
                    
                    flag_cargar_numero_uno= False
                    flag_cargar_numero_dos = False
                    flag_calcular_operaciones = True
                else:
                    if not flag_cargar_numero_uno:
                        imprimir_mensaje("primero debe cargar el numero uno")
                    else: 
                        imprimir_mensaje("Antes debe cargar el numero dos")

            case "4":
                
                if flag_calcular_operaciones:
                    mostrar_resultados(diccionario_operaciones)
                    num_uno = 0 
                    num_dos = 0
                else:
                    imprimir_mensaje("primero debe realizar el calculo")    
                    
            case "5":
                os._exit(0)    




