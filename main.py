from request_password import enter
from bitcoin_price import btc_price
from log4pi import init_log, log4pi
import requests
from i18n import i18n, LOCALES
import logging

from config import LANG

if __name__  == "__main__" : 

    # Inicializa logger principal de la ejecucion CLI.

    logger = init_log ( __name__ )
    log4pi ( logger, logging.DEBUG, f"Aplicación iniciada.")
    log4pi ( logger, logging.DEBUG, f"Idioma en uso: {LANG}.")

    # Solo consulta BTC cuando la autenticacion es correcta.

    if enter () : 
        try :
            salida = f"1 BTC = {btc_price ()} $"

            log4pi ( logger, logging.DEBUG, f" print: {salida}")
            print ( f"\n{salida}\n" )

        except requests.exceptions.ConnectionError :
            log4pi ( logger, logging.ERROR, i18n ("connection_failed" ), LOCALES )

        except requests.exceptions.Timeout :
            log4pi ( logger, logging.ERROR, i18n ( "request_timed_out" ), LOCALES )

        except requests.exceptions.HTTPError as e :
            log4pi ( logger, logging.ERROR, i18n ( "http_error_occurred: " + f"{e}" ), LOCALES )

        except requests.exceptions.RequestException as e :
            log4pi ( logger, logging.ERROR, i18n ( "an_error_occurred: " + f"{e}" ), LOCALES )
