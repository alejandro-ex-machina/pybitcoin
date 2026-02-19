# ------------------------------------------------------
# Levanta un API mínimo con los siguientes endpoints
# - (GET)  /    información
# - (POST) /BTC?secret=<hash>  devuelve el precio actual de Bicoin
# - (GET)  /SHA1/cadena
# - (POST) /ROT13?v=cadena
# el puerto en que se escucha está declarado en config.py
# -------------------------------------------------------

import codecs
import hashlib
from log4pi import init_log
from config import DEBUG
from config import PORT
from bitcoin_price import btc_price
from request_password import get_saved_password
from flask import Flask, jsonify, request

app = Flask ( __name__ )
logger = init_log ( __name__ )

@app.route( '/', methods=['GET'])

def root():
        # Endpoint informativo para comprobar disponibilidad del servicio.
        logger.info ( "/ endpoint" )
        return jsonify({ 'INFO' : 'Call /BTC endpoint via POST to obtaint last Bitcoin price'})

@app.route('/SHA1/<cadena>', methods=['GET'])
def sha1(cadena):
    # Utilidad de hash SHA1 para una cadena recibida por path.
    hash = hashlib.sha1(cadena.encode('utf-8'))
    return hash.hexdigest()

@app.route('/ROT13', methods=['POST'])

def rot13_post ():
    # Utilidad de codificacion ROT13 recibiendo v por query string.
    try:
        v = request.args.get('v') 
        encode = codecs.encode(v, 'rot_13')
        logger.info ( f"/ROT13 {encode}" )

        return jsonify ( {'ROT13' : codecs.encode(v, 'rot_13') } )
    
    except ValueError as e:
        logger.info ( f"{str(e)} Error 500" )
        return jsonify({'error': str(e)}), 500

@app.route('/BTC', methods=['POST'])

def btc_post ():
    # Devuelve BTC si el secret coincide con el hash almacenado.
    try:
        secret = request.args.get('secret') 
        saved  = get_saved_password ()

        if DEBUG :  
            print ( f"Secret: {secret}" )
            print ( f"Saved: {saved}" )

        retorno = jsonify({ 'ERROR' : "SECRET ERROR"})

        if ( secret == saved ) : retorno = jsonify({ 'BTC' : btc_price ()})
        logger.info ( "/BTC endpoint" )

        return retorno
    
    except ValueError as e:
        logger.info ( f"{str(e)} Error 500" )
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run ( port = PORT, debug = True )
    