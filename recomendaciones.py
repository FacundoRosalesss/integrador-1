def recomendaciones(error1, error2, error3, error4, error5, error6):
    """
    función para mostrar recomendaciones basadas en los errores detectados

    parametros:
    - error1: bool
    - error2: bool
    - error3: bool
    - error4: bool
    - error5: bool
    - error6: bool

    retorna:
    - None
    """
    print("\n--- Recomendaciones ---\n")

    if error1 == True:
        print("✔ Evaluar la posibilidad de actualizar el hardware o optimizar los procesos para reducir la carga.")

    if error2 == True  :
        print("✔ Revisar la configuración del sistema para mejorar la asignación de recursos.")

    if error3 == True:
        print("✔ Considerar la expansión del almacenamiento o la implementación de políticas de gestión de archivos.")

    if error4 == True:
        print("✔ Implementar medidas de escalabilidad para manejar el aumento de usuarios.")

    if error5 == True:
        print("✔ Activar y configurar el firewall para proteger el servidor.")

    if error6 == True:
        print("✔ Liberar espacio en disco y revisar los procesos activos para restaurar la operatividad del servidor.")

    print("\n--- Fin del diagnóstico ---\n")