from inputs import pedir_float, pedir_int, pedir_string
from archivos import guardar_servidores
from reglas_y_calculos import reglas_y_calculos
from recomendaciones import recomendaciones

def cargar_configuracion(servidores: dict):
    """
    Agrega un nuevo servidor directamente al diccionario en memoria RAM.
    """
    server_name = pedir_string("Ingrese nombre del servidor: ")

    if server_name in servidores:
        print("El nombre del servidor ya existe.")
        return
    
    admin_name = pedir_string("Ingrese nombre del administrador responsable: ")
    uso_cpu = pedir_float("Inserte uso de CPU (%): ", min_val=0, max_val=100)
    uso_ram = pedir_float("Inserte uso de memoria RAM (%): ", min_val=0, max_val=100)
    espacio_disco = pedir_float("Inserte espacio libre en disco (GB): ", min_val=0)
    cant_user = pedir_int("Inserte la cantidad de usuarios conectados: ", min_val=0)
    cant_proce = pedir_int("Inserte la cantidad de procesos activos: ", min_val=0)
    so = pedir_int("Indique el tipo de sistema operativo:\n1- Linux\n2- Windows\n3- macOS\n", min_val=1, max_val=3)
    firewall = pedir_int("Indique el estado del firewall:\n1- Activo\n2- Inactivo\n", min_val=1, max_val=2)
    server_tipo = pedir_int("Indique tipo del servidor:\n1- Web\n2- Base de datos\n3- Archivos\n", min_val=1, max_val=3)
    
    servidores[server_name] = {
        "administrador": admin_name,
        "cpu": uso_cpu,
        "ram": uso_ram,
        "procesos": cant_proce,
        "disco": espacio_disco,
        "so": so,
        "usuarios": cant_user,
        "firewall": firewall,
        "tipo": server_tipo
    }
    print(f"\nServidor '{server_name}' añadido temporalmente.")


def mostrar_configuracion(servidores: dict):
    """
    Muestra los servidores que están actualmente cargados en la memoria RAM.
    """
    if not servidores:
        print("\nNo hay servidores en la sesión actual.")
        return

    for id_servidor, servidor in servidores.items():
        print("------------------------")
        print(f"ID / Nombre: {id_servidor}")
        print(f"Administrador: {servidor['administrador']}")
        print(f"CPU: {servidor['cpu']}%")
        print(f"RAM: {servidor['ram']}%")
        print(f"Disco: {servidor['disco']} GB")
        print(f"Procesos: {servidor['procesos']}")
        
        if servidor['so'] == 1:
            print("Sistema operativo: Linux")
        elif servidor['so'] == 2:
            print("Sistema operativo: Windows")
        else:
            print("Sistema operativo: macOS")
            
        print(f"Usuarios: {servidor['usuarios']}")
        
        if servidor['firewall'] == 1:
            print("Firewall: Activo")
        else:
            print("Firewall: Inactivo")
            
        if servidor['tipo'] == 1:
            print("Tipo de servidor: Web")
        elif servidor['tipo'] == 2:
            print("Tipo de servidor: Base de datos")
        else:
            print("Tipo de servidor: Archivos")
        print("------------------------")


def modificar_configuracion(servidores: dict):
    """
    Modifica los datos de un servidor existente directamente en la memoria RAM.
    """
    servidor = pedir_string("\nIngrese el nombre del servidor a modificar: ")
    
    if servidor not in servidores:
        print("\nEl nombre del servidor no existe en esta sesión.")        
        return
    
    admin_name = pedir_string("Ingrese nombre del administrador responsable: ")
    uso_cpu = pedir_float("Inserte uso de CPU (%): ", min_val=0, max_val=100)
    uso_ram = pedir_float("Inserte uso de memoria RAM (%): ", min_val=0, max_val=100)
    espacio_disco = pedir_float("Inserte espacio libre en disco (GB): ", min_val=0)
    cant_user = pedir_int("Inserte la cantidad de usuarios conectados: ", min_val=0)
    cant_proce = pedir_int("Inserte la cantidad de procesos activos: ", min_val=0)
    so = pedir_int("Indique el tipo de sistema operativo:\n1- Linux\n2- Windows\n3- macOS\n", min_val=1, max_val=3)
    firewall = pedir_int("Indique el estado del firewall:\n1- Activo\n2- Inactivo\n", min_val=1, max_val=2)
    server_tipo = pedir_int("Indique tipo del servidor:\n1- Web\n2- Base de datos\n3- Archivos\n", min_val=1, max_val=3)
    
    servidores[servidor] = {
        "administrador": admin_name,
        "cpu": uso_cpu,
        "ram": uso_ram,
        "disco": espacio_disco,
        "procesos": cant_proce,
        "so": so,
        "usuarios": cant_user,
        "firewall": firewall,
        "tipo": server_tipo
    }
    print(f"\nCambios aplicados en memoria para '{servidor}'.")


def ejecutar_diagnostico(servidores: dict):
    """
    Envía los servidores actuales de la RAM al módulo de diagnóstico.
    """
    error1, error2, error3, error4, error5, error6 = reglas_y_calculos(servidores)
    recomendaciones(error1, error2, error3, error4, error5, error6)


def guardar_configuracion(servidores: dict):
    """
    Escribe el diccionario de la RAM en el archivo JSON.
    """
    guardar_servidores(servidores)
    print("\nCambios guardados exitosamente")