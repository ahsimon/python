class Employee:
    
    employee_id = 0
    employee_name =""

# create two objects of the Employee class
employee1 = Employee()
employee2 = Employee()


employee1.employee_id = 1001
print(f"Employee ID: {employee1.employee_id}")
employee1.employee_name="Angelica"


employee2.employee_id = 1002
print(f"Employee ID: {employee2.employee_id}")

employee3=Employee()
employee3.employee_id = "2001"

print(f"Employee ID: {employee3.employee_id}")