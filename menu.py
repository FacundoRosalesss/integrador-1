from inputs import pedir_int
from archivos import cargar_servidores
from funcionalidades import (
    cargar_configuracion, 
    mostrar_configuracion, 
    ejecutar_diagnostico, 
    guardar_configuracion, 
    modificar_configuracion
)

servidores_en_memoria = cargar_servidores()

def menu() -> int:
    print('\n--- SISTEMA DE DIAGNOSTICO Y CONFIGURACION DE SERVIDOR BASADO EN REGLAS  ---\n')
    print("1- Cargar configuración")
    print("2- Mostrar configuración")
    print("3- Modificar configuración")
    print("4- Ejecutar diagnóstico")
    print("5- Guardar configuración")
    print("6- Salir del programa")
    
    opcion = pedir_int("Ingrese una opción: ", min_val=1, max_val=6)
    
    match opcion:
        case 1:
            cargar_configuracion(servidores_en_memoria)
        case 2:
            mostrar_configuracion(servidores_en_memoria)
        case 3:
            modificar_configuracion(servidores_en_memoria)
        case 4:
            ejecutar_diagnostico(servidores_en_memoria)
        case 5:
            guardar_configuracion(servidores_en_memoria)
        case 6:
            print("Saliendo del programa...")
            
    return opcion