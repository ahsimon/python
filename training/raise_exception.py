
def print_five_items(data):
    
    if len(data) != 5:
        raise ValueError("The argument must have five elements")
    
    for item in data:
        print(item)

print_five_items([5, 2,3,4,1])