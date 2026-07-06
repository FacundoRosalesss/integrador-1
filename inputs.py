from validaciones import es_float
from validaciones import es_int

def pedir_float(
    mensaje: str, 
    min_val: float = 0, 
    max_val: float = 999999999999
    ) -> float:
    """
    input para pedir un numero flotante con validacion de rango

    Args:
    - mensaje: (str)
    - min_val: (float)
    - max_val: (float)

    Returns:
    - valor_float: (float)
    """

    while True:
        valor_float = input(mensaje)
        if es_float(valor_float):
            if min_val <= float(valor_float) <= max_val:
                return float(valor_float) # <--- Unica salida
        else:
            print(f"Por favor, ingrese un número entre {min_val} y {max_val}.")
        


def pedir_int(
    mensaje: str, 
    min_val: int = 0, 
    max_val: int = 999999999999
    ) -> int:
    """
    input para pedir un numero entero con validacion de rango

    Args:
    - mensaje: (str)
    - min_val: (int)
    - max_val: (int)

    Returns:
    - valor_int: (int)
    """
    
    while True:
            valor_int = input(mensaje)
            if es_int(valor_int) and min_val <= int(valor_int) <= max_val:
                return int(valor_int) # <--- Unica salida
            else:
                print(f"Por favor, ingrese un número entero entre {min_val} y {max_val}.")
            

def pedir_string(
    mensaje: str
    ) -> str:
    """
    input para pedir una cadena de texto con validación de longitud y formato

    Args:
    - mensaje: (str)

    Returns:
    - valor_string: (str)
    """

    while True:
        valor_string = input(mensaje)
        if len(valor_string) >= 5 and valor_string[0] != ' ':
            return valor_string # <--- Unica salida
        else:
            print("Entrada no válida. Ingrese una cadena de al menos 5 caracteres que no comience con un espacio.")
