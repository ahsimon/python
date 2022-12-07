import logging

logging.basicConfig(filename="otherfile.log", format="%(asctime)s - %(message)s", filemode="w", level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())


