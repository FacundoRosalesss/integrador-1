def recomendaciones(
    error1: int, 
    error2: int, 
    error3: int, 
    error4: int, 
    error5: int, 
    error6: int
    ) -> None:
    """
    función para mostrar recomendaciones basadas en los errores detectados

    Args:
    - error1: (bool)
    - error2: (bool)
    - error3: (bool)
    - error4: (bool)
    - error5: (bool)
    - error6: (bool)

    Returns:
    - None
    """
    print("\n--- Recomendaciones ---\n")

    if error1:
        print("✔ Evaluar la posibilidad de actualizar el hardware o optimizar los procesos para reducir la carga.")

    if error2  :
        print("✔ Revisar la configuración del sistema para mejorar la asignación de recursos.")

    if error3:
        print("✔ Considerar la expansión del almacenamiento o la implementación de políticas de gestión de archivos.")

    if error4:
        print("✔ Implementar medidas de escalabilidad para manejar el aumento de usuarios.")

    if error5:
        print("✔ Activar y configurar el firewall para proteger el servidor.")

    if error6:
        print("✔ Liberar espacio en disco y revisar los procesos activos para restaurar la operatividad del servidor.")

    print("\n--- Fin del diagnóstico ---\n")