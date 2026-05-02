print ("hola")


uso_cpu = float(input ("Inserte uso de CPU (%): "))
uso_ram = float(input ("Insete uso de memoria RAM (%): " ))
espacio_disco = float(input ("Indique espacio libre en el disco (GB): "))
cant_user = int(input ("Indique la cantidad de usuarios conectados: "))
cant_proce = int(input ("Indique la cantidad de procesos activos: "))
so = int(input ("Indique EL tipo de sistema operativo:\n1- Linux\n2- Windows defender\n"))
firewall = int(input ("Indique el destado del firewall:\n1- Activo\n2- Inactivo\n"))
server_tipo = int(input ("Indique tipo del servidor:\n1- Web\n2- Base de datos\n3- Archivos\n"))
server_name = input ("Ingrese nombre del servidor: ")
admin_name = input ("Ingrese nombre del administrador responsable: ")

print(f'\n--- Bienvenido {admin_name} reporte de evaluación de servidor: "{server_name}" ---')
