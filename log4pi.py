from config import LOG_FILENAME
import time
import logging

def init_log ( logger_name ) :
    logger = logging.getLogger ( f"[{logger_name}]" )
    logging.basicConfig ( filename = LOG_FILENAME , level = logging.DEBUG, encoding='utf-8' )
    return logger

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
    
    loger = init_log ( __name__ )

    log4pi  (loger, logging.DEBUG, "Log inicializado en log4pi" )
