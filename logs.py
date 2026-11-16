# configuración del sistema de registros (logs)

import logging

# archivo de texto donde se guardarán los registros
LOG_FILE = "sistema_fj.log"

# configuración general del registro de eventos
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)

def registrar_evento(mensaje):
    # guarda una acción normal del sistema
    logging.info(mensaje)

def registrar_error(mensaje):
    # guarda un error o excepción cuando algo falla
    logging.error(mensaje)