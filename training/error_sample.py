
def divide_integers():
    while True:
        try:
            a = int(input("Please enter the numerator: "))
            b = int(input("Please enter the denominator: "))
            print(a / b)
        except ZeroDivisionError:
            print("Please enter a valid denominator.")


divide_integers()