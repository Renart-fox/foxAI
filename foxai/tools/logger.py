import logging
import logging.handlers
from sys import stdout

_levelToName = {
    logging.CRITICAL: 'CRITICAL',
    logging.ERROR: 'ERROR',
    logging.WARNING: 'WARNING',
    logging.INFO: 'INFO',
    logging.DEBUG: 'DEBUG',
    logging.NOTSET: 'NOTSET',
}


def create_logger(caller_name: str, log_level: int = 10):
    """
        Returns a logger with a name based on its caller and its logging level.

        All logs will be redirected to stdout and a Rotating File named after both given arguments.

        If an error occurs, returns None
    """
    if not isinstance(caller_name, str):
        logging.info('Attr caller_name must be of type string.')
        return None
    if not caller_name:
        logging.info('Attr caller_name must not be empty when creating a logger.')
        return None
    if not isinstance(log_level, int):
        logging.info('Attr log_level is invalid. Expected integer, got {log_level}')
        return None
    if log_level//10-5 > 0 or log_level % 10 != 0:
        logging.info('Attr log_level is invalid. Expected 0, 10, 20, 30, 40 or 50.')
        return None

    logging_logger = logging.getLogger(caller_name)
    logging_logger.setLevel(log_level)
    l_sh = logging.StreamHandler(stream=stdout)
    l_sh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logging_logger.addHandler(l_sh)
    l_rfh = logging.handlers.RotatingFileHandler(
        '{}{}.log'.format(caller_name, _levelToName[log_level]),
        mode='rw',
        maxBytes=1024)
    l_rfh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logging_logger.addHandler(l_rfh)

    return logging_logger
