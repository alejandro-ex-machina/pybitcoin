from config import LOG_FILENAME
from config import ENCODING
import time
import logging
import os
import platform
import datetime

def init_log ( logger_name ) :
    time_tuple = get_creation_date(LOG_FILENAME)
    logger = logging.getLogger ( f"[{logger_name}]" )
    logging.basicConfig ( filename = LOG_FILENAME , level = logging.DEBUG, encoding=ENCODING )
    return logger

def print_time_tuple ( time_tuple ) :
    year, month, day = time_tuple.tm_year, time_tuple.tm_mon, time_tuple.tm_mday
    print ( f"{year}-{month:02d}-{day:02d}" ) 

def today () :
    ret = datetime.datetime.now().strftime("%Y-%m-%d")
    print ( ret )
    return ret

def get_creation_date ( path_to_file ) :
    creation_time = os.path.getctime(path_to_file)
    time_tuple = time.localtime( creation_time )
    #print_time_tuple ( time_tuple )
    return time_tuple

def _format_datetime ( t ) :
    return time.strftime ( "%d/%m/%Y %H:%M:%S", t )

def log4pi ( logger, severity, mensaje ) :

    cadena = f"{ _format_datetime ( time.localtime() ) } {mensaje}"

    # logging.log permite despachar por nivel sin repetir ramas por severidad.
    
    if isinstance(severity, int):
        logger.log ( severity, cadena )

    else:
        logger.warning ( cadena )


if __name__ == "__main__" :  

    loger = init_log ( LOG_FILENAME )