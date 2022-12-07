import logging



logging.basicConfig(filename="otherfile.log", format="%(asctime)s - %(message)s", filemode="w", level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())

def f(i):
    try:
        g(i)
    except IndexError:
        print("Please enter a valid index")
        logging.error("The variable is not numeric.")
def g(i):
    a = "Hello"
    return a[i]

logging.info(f(10))
