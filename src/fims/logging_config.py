import logging
import sys

def setup_logger() -> logging.Logger:
    logger = logging.getLogger("fims")
    if logger.handlers:
        return logger  # avoid double handlers when imported multiple times

    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("[%(levelname)s] %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger


logger = setup_logger()
