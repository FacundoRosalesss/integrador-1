from menu import menu
from reglas_y_calculos import reglas_y_calculos
from recomendaciones import recomendaciones


# Menu
uso_cpu, uso_ram, porcentaje_carga, espacio_disco, cant_user, cant_proce, so, firewall, server_tipo, server_name, admin_name = menu()

# Reglas y cálculos
error1, error2, error3, error4, error5, error6 = reglas_y_calculos(uso_cpu, uso_ram, porcentaje_carga, espacio_disco, cant_user, cant_proce, so, firewall, server_tipo, server_name, admin_name)

# Recomendaciones
recomendaciones(error1, error2, error3, error4, error5, error6)

