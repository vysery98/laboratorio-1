# Importación de librerías
import logging
import json

# Configuración de Logs
def setupLogs():
    logs = logging.getLogger("api_logger")
    logs.setLevel(logging.INFO)

    # Definir el archivo de salida y formato de mensaje
    handler = logging.FileHandler("app.log") # Archivo a crear para registrar logs
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)

    logs.addHandler(handler)

    return logs

# Inicialización global del logger
logs = setupLogs()

# Función para registrar un evento específico en el archivo - formato JSON
def logEvent(evento, data):
    logEntry = {
        "evento": evento,
        "datos": data
    }
    # Conversión del diccionario a cadena JSON
    logs.info(json.dumps(logEntry))