from typing import Final

# --------------------------------------------
# Parametros de configuracion de la aplicacion
# --------------------------------------------

DEBUG:         Final[bool] = False
PORT:          Final[int]  = 8080
URL_API_BTC:   Final[str]  = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
PWD_FILENAME:  Final[str]  = "password.sha256"
LOG_FILENAME:  Final[str]  = "log/app.log"
LANG:          Final[str]  = "es"
LANG_PATH:     Final[str]  = "./translations/"
ENCODING:      Final[str]  = "utf-8"