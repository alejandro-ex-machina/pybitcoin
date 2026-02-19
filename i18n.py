import json
from config import LANG
from config import LANG_PATH

def LOCALES () : return load_json ( f"{LANG_PATH}{LANG}.json" )

def load_json ( FILENAME ) :
    # Carga el catalogo JSON del idioma activo.

    with open ( FILENAME , 'r' ) as file :
        saved = file.readlines()
        
        with open ( FILENAME, 'r', encoding='utf-8') as archivo:
                
            datos = json.load ( archivo )
            return datos

def i18n ( cadena, datos ) :
    # Busca una clave de traduccion dentro de la lista de diccionarios.
    for d in datos:
        if cadena in d:
            return d.get(cadena) 
        
    return f"{cadena} {LANG} :: <Not found>"

        
if __name__ == '__main__':
    pass
