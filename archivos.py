import json

SERVIDORES = "data/servidores.json"

def cargar_servidores():
    """
    funcion para cargar la informacion del archivo json
    
    arg:
        None
    
    returns:
        archivo: lists
    """
    with open(SERVIDORES, "r", encoding="utf-8") as archivo:
        return json.load(archivo)
    
def guardar_servidores(
    servidores:list
    ) -> None:
    """
    funcion para guardar la informacion en el archivo json
    
    arg:
        servidores: list
    
    return:
        None
    """
    with open(SERVIDORES, "w", encoding="utf-8") as archivo:
        json.dump(servidores, archivo, indent=4, ensure_ascii=False)
        

        
