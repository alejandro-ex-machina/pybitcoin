# pybitcoin

Aplicación en Python para consultar el precio de Bitcoin (BTC/USDT) en Binance, con control de acceso por contraseña hash, soporte básico de internacionalización y registro en log.

## Características

- Solicita contraseña por terminal (máximo 3 intentos).
- Valida la contraseña comparando su hash con `password.sha256`.
- Consulta el precio de BTC usando la API pública de Binance.
- Guarda eventos en `log/app.log`.
- Soporta mensajes en varios idiomas (`es`, `en`, `de`).
- Incluye una API Flask con endpoints utilitarios y endpoint protegido para BTC.

## Estructura del proyecto

- `main.py`: punto de entrada en modo CLI.
- `request_password.py`: lógica de autenticación y lectura del hash guardado.
- `bitcoin_price.py`: consulta del precio de BTC.
- `api.py`: API Flask con endpoints `/`, `/SHA1/<cadena>`, `/ROT13`, `/BTC`.
- `log4pi.py`: inicialización y escritura de logs.
- `console_utils.py`: utilidades de consola (limpieza de pantalla).
- `i18n.py`: carga de traducciones y resolución de textos.
- `config.py`: parámetros de configuración.
- `translations/*.json`: catálogos de traducción.
- `password.sha256`: hash esperado para autorizar acceso.

## Requisitos

- Python 3.11+ (probado en entorno con Python 3.14).
- Dependencias:
  - `requests`
  - `flask` (si se usa `api.py`)

Instalación:

```bash
pip install requests flask
```

## Configuración

La configuración está centralizada en `config.py`:

- `DEBUG`: activa salidas de depuración.
- `URL_API_BTC`: URL del ticker BTCUSDT.
- `PWD_FILENAME`: archivo con hash de contraseña.
- `LOG_FILENAME`: ruta de log.
- `LANG`: idioma activo (`es`, `en`, `de`).
- `LANG_PATH`: carpeta de traducciones.
- `PORT`: puerto de la API Flask.

## Uso (CLI)

Ejecutar:

```bash
python main.py
```

Flujo:

1. Pide contraseña (1234).
2. Si valida, consulta el precio de BTC.
3. Muestra en pantalla `1 BTC = <precio> $`.

## Uso (API Flask)

Ejecutar:

```bash
python api.py
```

Endpoints:

- `GET /`: información general.
- `GET /SHA1/<cadena>`: devuelve SHA1 de la cadena.
- `POST /ROT13?v=<cadena>`: devuelve ROT13 del valor recibido.
- `POST /BTC?secret=<hash>`: devuelve precio BTC si `secret` coincide con `password.sha256`.

## Seguridad y observaciones

- La autenticación compara hash con un valor local; es un mecanismo básico.
- La app usa `shake_256(...).hexdigest(20)` para validar contraseña.
- Se recomienda no registrar datos sensibles en logs en producción.
- El directorio de traducciones se llama `translations`, y está referenciado así en `config.py`.

## Mejoras pendientes

- Capturar errores de red y timeouts en la consulta de Binance.
- Añadir tests unitarios para autenticación, i18n y API.
