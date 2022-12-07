import logging

logging.basicConfig(filename="Pythonlogfile.log", format="%(asctime)s - %(message)s", filemode="w", level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())
logging.debug("This message is logged to the file.")
logging.info("Less severe information is also logged to the file.")
logging.warning("Warning messages are logged, too.")

a = "text"

try:
    logging.info(str(a**2))
except TypeError:
    logging.error("The variable is not numeric.")

logging.shutdown()