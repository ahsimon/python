
students = {"Angelica": 37, "Lakshmi": 30}
def print_student_age():
    while True:
        try:
            name = input("Please enter the name of the student: ")
            print(students[name])
            break
        except:
            print("This name is not registered")
    

print_student_age()
