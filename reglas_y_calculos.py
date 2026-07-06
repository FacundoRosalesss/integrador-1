from archivos import cargar_servidores

def reglas_y_calculos(
) -> tuple[bool, bool, bool, bool, bool, bool]:
    """
    función para evaluar las reglas y cálculos del diagnóstico del servidor elegido

    Args:
        servidores: dict

    Returns:
    - error1: (bool)
    - error2: (bool)
    - error3: (bool)
    - error4: (bool)
    - error5: (bool)
    - error6: (bool)
    """
    
    servidores = cargar_servidores()
    
    server_name = input("\nIngrese el nombre del servidor a diagnosticar: ")
    
    if not servidores:
        print("No hay servidores registrados.")
        return False, False, False, False, False, False
    
    for id_servidor, servidor in servidores.items():
        if servidor == server_name:
            uso_cpu = servidor["cpu"]
            uso_ram = servidor["ram"]
            porcentaje_carga = (uso_cpu + uso_ram) / 2
            espacio_disco = servidor["disco"]
            cant_user = servidor["usuarios"]
            cant_proce = servidor["procesos"]
            so = servidor["so"]
            firewall = servidor["firewall"]
            server_tipo = servidor["tipo"]
            server_name = servidor["nombre"]
            admin_name = servidor["administrador"]
            break
    else:
        print("El nombre del servidor no existe.")
        return False, False, False, False, False, False
        
    
    if 40 <= float(uso_cpu) <= 75 and float(espacio_disco) >= 50:
        print(f"El uso de CPU se encuentra en el rango operativo esperado. Uso actual: {uso_cpu}%. Espacio libre: {espacio_disco}GB.")

    if 40 <= float(uso_ram) <= 75 and float(espacio_disco) >= 50:
        print(f"El uso de RAM se encuentra en el rango operativo esperado. Uso actual: {uso_ram}%. Espacio libre: {espacio_disco}GB.")

    print(f"El porcentaje de carga del servidor es: {porcentaje_carga}%.\n")

    if (uso_cpu >= 90 or uso_ram >= 90) and cant_proce >= 100:
        print(f"‼️ [Error 140] Sobrecarga crítica de hardware detectada. Usuarios: {cant_user}, Procesos: {cant_proce}, CPU: {uso_cpu}%, RAM: {uso_ram}%.")
        error1 = True
    else:
        error1 = False

    if cant_proce > 0:        
        if (cant_user / cant_proce) > 20:
            print(f"‼️ [Error 340] Cantidad de usuarios por proceso inusualmente alta. Usuarios: {cant_user}, Procesos: {cant_proce}.")
            error2 = True
        else:
            error2 = False
    else:
        error2 = False

    if int(server_tipo) == 3 and (int(cant_user) > 15 or float(espacio_disco) < 50):
        print(f"‼️ [Error 233] Servidor de archivos con alta demanda o poco espacio. Usuarios: {cant_user}, Espacio libre: {espacio_disco}GB.")
        error3 = True
    else:
        error3 = False

    if int(cant_user) > 50 and int(server_tipo) == 1:
        print(f"‼️ [Error 301] El servidor Web está llegando al límite de usuarios. cant_user: {cant_user}.")
        error4 = True
    else:
        error4 = False

    if int(firewall) != 1 and int(cant_user) > 0:
        print("‼️ [Error 530] El servidor está expuesto con usuarios activos y sin firewall.")
        error5 = True
    else:
        error5 = False

    if float(espacio_disco) == 0 and float(cant_proce) >= 1:
        print("‼️ [Error 240] Recursos agotados, el servidor no puede operar.")
        error6 = True
    else:
        error6 = False

    return error1, error2, error3, error4, error5, error6