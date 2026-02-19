import json
from config import LANG
from config import LANG_PATH
from config import ENCODING
from typing import Final

def load_json ( FILENAME ) :
    # Carga el catalogo JSON del idioma activo.

    with open ( FILENAME , 'r' ) as file :
        saved = file.readlines()
        
        with open ( FILENAME, 'r', encoding=ENCODING ) as archivo:
                
            datos = json.load ( archivo )
            return datos

def i18n ( cadena, datos ) :
    # Busca una clave de traduccion dentro de la lista de diccionarios.
    for d in datos:
        if cadena in d:
            return d.get(cadena) 
        
    return f"{cadena} {LANG} :: <Not found>"

LOCALES :  Final[str]  = load_json ( f"{LANG_PATH}{LANG}.json" )

if __name__ == '__main__':
    pass
