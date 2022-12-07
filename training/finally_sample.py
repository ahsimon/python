import logging
def divide_integers():
    while True:
        try:
            a = int(input("Please enter the numerator: "))
            b = int(input("Please enter the denominator: "))
            result = a / b
        except (ZeroDivisionError, ValueError):
            print("Please enter valid integers. The denominator can't be zero")
            logging.error("Please enter valid integers. The denominator can't be zero")
        else:
            print(result)
        finally:
            print("Inside the finally clause")

divide_integers()