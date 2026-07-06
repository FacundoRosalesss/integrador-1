def es_float(
    cadena: str
    ) -> bool:
    """
    verifica que cadena de caracteres sea float
    
    Args:
    cadena: str
    
    Returns:
    
    """
    if not cadena:
        return False

    puntos = 0

    for i in range(len(cadena)):
        if cadena[i] == ".":
            puntos += 1
        elif cadena[i] < "0" or cadena[i] > "9":
            return False
        
    return puntos <= 1

def es_int(
    cadena: str
    ) -> bool:
    """
    verifica que cadena sea un integer
    """

    if not cadena:
        return False

    for i in range(len(cadena)):
        if cadena[i] < "0" or cadena[i] > "9":
            return False

    return True