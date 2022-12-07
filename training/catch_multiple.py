def divide_integers():
    while True:
        try:
            a = int(input("Please enter the numerator: "))
            b = int(input("Please enter the denominator: "))
            print(a / b)
        except ZeroDivisionError as e:
            print(type(e))
            print(e)
            print(e.args)
        except ValueError as e:
            print(type(e))
            print(e)
            print(e.args)    
divide_integers()