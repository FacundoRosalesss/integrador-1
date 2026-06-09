from inputs import pedir_float, pedir_int, pedir_string

def menu():
    """
    Muestra el menú de opciones para ingresar los datos del servidor.

    retorna:
    - uso_cpu: float
    - uso_ram: float
    - porcentaje_carga: float
    - espacio_disco: float
    - cant_user: int
    - cant_proce: int
    - so: int
    - firewall: int
    - server_tipo: int
    - server_name: str
    - admin_name: str
    """
    print(f'\n--- SISTEMA DE DIAGNOSTICO Y CONFIGURACION DE SERVIDORBASADO EN REGLAS  ---\n')

    uso_cpu = pedir_float("Inserte uso de CPU (%): ", min_val=0, max_val=100)

    uso_ram = pedir_float("Inserte uso de memoria RAM (%): ", min_val=0, max_val=100)

    porcentaje_carga = (uso_cpu + uso_ram) / 2

    espacio_disco = pedir_float("Inserte espacio libre en disco (GB): ", min_val=0)

    cant_user = pedir_int("Inserte la cantidad de usuarios conectados: ", min_val=0)

    cant_proce = pedir_int("Inserte la cantidad de procesos activos: ", min_val=0)

    so = pedir_int("Indique EL tipo de sistema operativo:\n1- Linux\n2- Windows\n3- macOS\n", min_val=1, max_val=3)

    firewall = pedir_int("Indique el numero del estado del firewall:\n1- Activo\n2- Inactivo\n", min_val=1, max_val=2)

    server_tipo = pedir_int("Indique tipo del servidor:\n1- Web\n2- Base de datos\n3- Archivos\n", min_val=1, max_val=3)

    server_name = pedir_string("Ingrese nombre del servidor: ")
    admin_name = pedir_string("Ingrese nombre del administrador responsable: ")

    print(f'\n--- Bienvenido {admin_name} reporte de evaluación de servidor: "{server_name}" ---\n')
    
    return uso_cpu, uso_ram, porcentaje_carga, espacio_disco, cant_user, cant_proce, so, firewall, server_tipo, server_name, admin_name