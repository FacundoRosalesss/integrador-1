
# ENTRADA DE DATOS

uso_cpu = float(input ("Inserte uso de CPU (%): "))
while uso_cpu < 0:
    uso_cpu = float(input ("reincierte un numero positivo CPU (%): "))

uso_ram = float(input ("Insete uso de memoria RAM (%): " ))
while uso_ram < 0:
    uso_ram = float(input ("reincierte un numero positivo memoria RAM (%): " ))

porcentaje_carga = (uso_cpu + uso_ram) / 2

espacio_disco = float(input ("Indique espacio libre en el disco (GB): "))
while espacio_disco < 0:
    espacio_disco = float(input ("reincierte numero positivo en el disco (GB): "))

cant_user = int(input ("Indique la cantidad de usuarios conectados: "))
while cant_user < 0:
    cant_user = int(input ("reincierte un numero positivo de usuarios conectados: "))

cant_proce = int(input ("Indique la cantidad de procesos activos: "))
while cant_proce < 0:
    cant_proce = int(input ("reincierte un numero positivo de procesos activos: "))

so = int(input ("Indique EL tipo de sistema operativo:\n1- Linux\n2- Windows\n3- macOS\n"))
while so < 1 or so > 3:
    so = int(input ("Indique EL tipo de sistema operativo:\n1- Linux\n2- Windows\n3- macOS\n"))

firewall = int(input ("Indique el numero del estado del firewall:\n1- Activo\n2- Inactivo\n"))
while firewall < 1 or firewall > 2:
    firewall = int(input ("Indique el numero del estado del firewall:\n1- Activo\n2- Inactivo\n"))

server_tipo = int(input ("Indique tipo del servidor:\n1- Web\n2- Base de datos\n3- Archivos\n"))
while server_tipo < 1 or server_tipo > 3:
    server_tipo = int(input ("Indique tipo del servidor:\n1- Web\n2- Base de datos\n3- Archivos\n"))

server_name = str(input ("Ingrese nombre del servidor: "))
admin_name = str(input ("Ingrese nombre del administrador responsable: "))

print(f'\n--- Bienvenido {admin_name} reporte de evaluación de servidor: "{server_name}" ---\n')

# VARIABLES CALCULADAS

if 40 <= uso_cpu <= 75 and espacio_disco >= 50:
    print(f"El uso de CPU se encuentra en el rango operativo esperado. Uso actual: {uso_cpu}%. Espacio libre: {espacio_disco}GB.")

if 40 <= uso_ram <= 75 and espacio_disco >= 50:
    print(f"El uso de RAM se encuentra en el rango operativo esperado. Uso actual: {uso_ram}%. Espacio libre: {espacio_disco}GB.")

print(f"El porcentaje de carga del servidor es: {porcentaje_carga}%.")

if uso_cpu >= 90 or uso_ram >= 90 and cant_proce >= 100:
    print(f"‼️ Sobrecarga crítica de hardware detectada. Usuarios: {cant_user}, Procesos: {cant_proce}, CPU: {uso_cpu}%, RAM: {uso_ram}%.")
    error1 = True
else:
    error1 = False

if cant_user / cant_proce > 20:
    print(f"‼️ Cantidad de usuarios por proceso inusualmente alta. Usuarios: {cant_user}, Procesos: {cant_proce}.")
    error2 = True   
else:
    error2 = False

if server_tipo == 3 and cant_user > 15 and espacio_disco < 50:
    print(f"‼️ Servidor de archivos con alta demanda y poco espacio. Usuarios: {cant_user}, Espacio libre: {espacio_disco}GB.")
    error3 = True
else:
    error3 = False

if cant_user > 50 and server_tipo == 1:
    print(f"‼️ El servidor Web está llegando al límite de usuarios. cant_user: {cant_user}.")
    error4 = True
else:
    error4 = False

if not firewall == 1 and cant_user > 0:
    print(f"‼️ El servidor está expuesto con usuarios activos y sin firewall.")
    error5 = True
else:
    error5 = False

if espacio_disco == 0 and cant_proce >= 1:
    print(f"‼️ Recursos agotados, el servidor no puede operar.")
    error6 = True
else:
    error6 = False

print("\n--- Recomendaciones ---\n")

# RECOMENDACIONES

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

