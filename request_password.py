# ---------------------------------------------------
# Pide por pantalla una password, calcula su sha256
# y lo compara con una versión guardada en un 
# archivo declarado en config.py
# ---------------------------------------------------

from config import PWD_FILENAME 
from config import DEBUG

import hashlib
import getpass
import logging

from log4pi import init_log, log4pi
from console_utils import cls
from i18n import i18n, LOCALES

logger = init_log ( __name__ )

def get_saved_password () :
    # Lee el hash almacenado para validar el acceso.
    try :
        with open ( PWD_FILENAME, 'r' ) as file :
            saved = file.readlines()[0].strip()
            return saved

    except FileNotFoundError :
        print ( f"Error: File {PWD_FILENAME} not found." )
        log4pi ( logger, logging.ERROR, f"{PWD_FILENAME} no encontrado" )
    
    except PermissionError :
        print ( "Error: No permission to read the file." )
        log4pi ( logger, logging.ERROR, f"Sin permiso para leer {PWD_FILENAME}" )
    
    except IOError as e :
        print ( f"Error reading file: {e}" )
        log4pi ( logger, logging.ERROR, f"Error leyendo {PWD_FILENAME} excepcion: {e}" )

def request_password () :
    # Captura password y compara su hash con el valor persistido.
    saved    = get_saved_password ()
    password = getpass.getpass ( prompt = i18n("enter_password", LOCALES ()),  echo_char = '*' )
    digest   = hashlib.shake_256 ( password.encode( 'utf-8') ).hexdigest( 20 )

    if DEBUG :  
        print ( f"Password: {password}" )
        print ( f"Saved: {saved}" )
        print ( f"Digest: {digest}" )

    # logger.info ( f"Input {digest} - Stored {saved}" )

    if digest != saved :
        log4pi ( logger, logging.WARNING, f"Usuario no autorizado con password sha256 {digest}." )
        return False
    else :
        msg = f"Usuario autorizado con password sha256 {digest}."
        log4pi ( logger, logging.INFO, msg )
        return True

def enter () :

    # Reintenta autenticacion hasta 3 veces antes de devolver error.
    
    cls ()

    password_ok = False
       
    for i in range ( 1, 4 ):  
        
        password_ok = request_password ()

        if password_ok : 
            print ( i18n ( "password_ok", LOCALES () ) )
            break
        else :
            print ( i18n ( "wrong_password", LOCALES () ) )

    return password_ok 
        
if __name__ == "__main__" :  
    
    enter ()    
