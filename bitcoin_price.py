# ------------------------------------------------
# btc_price () devuelve el precio actual de Bicoin
# ------------------------------------------------

import requests
import logging

from config import URL_API_BTC
from log4pi import init_log, log4pi

logger = init_log ( __name__ )

def btc_price () :
    # Consulta el ticker BTCUSDT y devuelve el precio como float.
    response = requests.get ( URL_API_BTC )
    data     = response.json()

    cotizacion = float ( data [ "price" ] )
    log4pi ( logger, logging.INFO, f"request {URL_API_BTC} - response {cotizacion}" )
    log4pi ( logger, logging.INFO, f"response {cotizacion}" )
    
    return cotizacion

if __name__ == "__main__" :  

    print ( btc_price () )
