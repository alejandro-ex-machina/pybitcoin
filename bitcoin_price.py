# ------------------------------------------------
# btc_price () devuelve el precio actual de Bicoin
# ------------------------------------------------

import requests
import logging

from config import URL_API_BTC
from log4pi import init_log, log4pi
from i18n import i18n, LOCALES
cotizacion = 0.0
logger = init_log ( __name__ )

def btc_price () :
    # Consulta el ticker BTCUSDT y devuelve el precio como float.
    
    try :
        response = requests.get( URL_API_BTC, timeout = 5 )
        response.raise_for_status()  # Raises HTTPError for bad status codes
        data     = response.json()

        log4pi ( logger, logging.DEBUG, f"request {URL_API_BTC} " )      
        log4pi ( logger, logging.DEBUG, f"response {response.status_code} - {response.text}" )
        
        return float ( data [ "price" ] )

    except requests.exceptions.ConnectionError :
        log4pi ( logger, logging.ERROR, i18n ("connection_failed", LOCALES ) )
        print ( i18n ("connection_failed", LOCALES ) )

    except requests.exceptions.Timeout :
        log4pi ( logger, logging.ERROR, i18n ( "request_timed_out", LOCALES ) )
        print ( i18n ( "request_timed_out", LOCALES ) )

    except requests.exceptions.HTTPError as e :
        log4pi ( logger, logging.ERROR, i18n ( "http_error_occurred", LOCALES ) + f"{e}" )
        print ( i18n ( "http_error_occurred" + f"{e}", LOCALES ) )  

    except requests.exceptions.RequestException as e :
        log4pi ( logger, logging.ERROR, i18n ( "an_error_occurred", LOCALES ) + f"{e}" )
        print ( i18n ( "an_error_occurred" + f"{e}", LOCALES ) )

if __name__ == "__main__" :  

    print ( btc_price () )
