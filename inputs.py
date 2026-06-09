def pedir_float(mensaje, min_val=0, max_val=999999999999):
    """
    input para pedir un numero flotante con validacion de rango

    parametros:
    - mensaje: str
    - min_val: float
    - max_val: float

    retorna:
    - valor_float: float
    """
    i = 0
    while i < 1:
        try:
            valor_float = float(input(mensaje))
            if min_val <= valor_float <= max_val:
                i += 1
                return valor_float
            else:
                print(f"Por favor, ingrese un número entre {min_val} y {max_val}.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")


def pedir_int(mensaje, min_val=0, max_val=999999999999):
    """
    input para pedir un numero entero con validacion de rango

    parametros:
    - mensaje: str
    - min_val: int
    - max_val: int

    retorna:
    - valor_int: int
    """
    i = 0
    while i < 1:
        try:
            valor_int = int(input(mensaje))
            if min_val <= valor_int <= max_val:
                i += 1
                return valor_int
            else:
                print(f"Por favor, ingrese un número entero entre {min_val} y {max_val}.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

def pedir_string(mensaje):
    """
    input para pedir una cadena de texto con validación de longitud y formato

    parametros:
    - mensaje: str

    retorna:
    - valor_string: str
    """
    i = 0
    while i < 1:
        valor_string = input(mensaje)
        if len(valor_string) >= 5 and valor_string[0] != ' ':
            i += 1
            return  valor_string
        else:
            print("Entrada no válida. Ingrese una cadena de al menos 5 caracteres que no comience con un espacio.")
