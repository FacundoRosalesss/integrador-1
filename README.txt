Sistema de Diagnóstico y Configuración de Servidor Basado en Reglas
Informacion breve del sistema.
El sistema pide al usuario informacion del servidor para analizar, recomendar, mejorar y prevenir posibles errores del mismo.
Caraterististicas del codigo
funciones propias
validaciones de datos de entradas
Organización lógica del sistema en múltiples archivos
Separación en funciones
Mejora en mantenibilidad y legibilidad
Idioma utilizado
- https://es.wikipedia.org/wiki/Python
Version utilizada de python
Python 3.13.7 (64bit)
Guia de pasos para probar el codigo
Copiar el https
Crear una carpeta en escritorio, abrirla, seleccionar la opcion de abrir con git bash here
Poner el comando git clone y el https
abrir con visual studio code
Recomendaciones para el servidor
def recomendaciones(error1, error2, error3, error4, error5, error6):
    """
    función para mostrar recomendaciones basadas en los errores detectados
    parametros:
    - error1: bool
    - error2: bool
        print("\n--- Recomendaciones ---\n")
    if error1 == True:
        print("✔ Evaluar la posibilidad de actualizar el hardware o optimizar los procesos para reducir la carga.")
    if error2 == True  :
        print("✔ Revisar la configuración del sistema para mejorar la asignación de recursos.")
Datos de entrada
def menu():
    """
    Muestra el menú de opciones para ingresar los datos del servidor.
    retorna:
    - uso_cpu: float
    - uso_ram: float
    uso_cpu = pedir_float("Inserte uso de CPU (%): ", min_val=0, max_val=100)
    uso_ram = pedir_float("Inserte uso de memoria RAM (%): ", min_val=0, max_val=100)
Integrantes del proyecto
Brian mendieta
Facundo rosales
Lucio denegris
Luciano toledo