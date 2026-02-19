from request_password import enter
from bitcoin_price import btc_price
from log4pi import init_log, log4pi
import logging

from config import LANG

if __name__  == "__main__" : 

    # Inicializa logger principal de la ejecucion CLI.

    logger = init_log ( __name__ )
    log4pi ( logger, logging.DEBUG, f"Aplicación iniciada.")
    log4pi ( logger, logging.DEBUG, f"Idioma en uso: {LANG}.")

    # Solo consulta BTC cuando la autenticacion es correcta.
    if enter () : 
        salida = f"1 BTC = {btc_price ()} $"

        log4pi ( logger, logging.DEBUG, f" print: {salida}")
        print ( f"\n{salida}\n" )


