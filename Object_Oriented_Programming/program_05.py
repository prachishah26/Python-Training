# Create class Person:
# Name,DOB,City,Contact No

# Create class Employee (Inherit person class)
# employee id
# joining date
# salary
# department
# post

# Employee manager class
# Add/Remove Employee, Get all employees list, get employee by his name, get all employees by his/her department,
# Task:
# Add few employees
# Print all the employees
# Find an employee with the name
# Print all employees with department Finance
# Find all employees whose salary is greater than 50000
# Find all employees whose salary is between 50000-100000
# Find a list of employees who are joined in the current year
# Find all employees who are from Mirzapur
# Find employees whose birthday in the current month
# Sort employee list with salary in descending order

# -----------------------------------------------------------------------------------------
from traceback import print_exc

class person:
    def __init__(self,name, dob, city, contact_no):
        self.name = name
        self.dob = dob
        self.city = city
        self.contact_no = contact_no

class Employee(person):
    identity = 100
    def __init__(self,name, dob, city, contact_no,joining_date,salary,department,post):
        super().__init__(name, dob, city, contact_no)
        self.employee_id = Employee.identity
        self.joining_date = joining_date
        self.salary = salary
        self.department = department
        self.post = post
        Employee.identity += 1

class Employee_manager():
    def __init__(self):
        self.total_employees = []
    def show_employees(self):
        if len(self.total_employees) != 0:
            for employee in self.total_employees:
                print(f"Employee id : {employee.employee_id}, Name of employee : {employee.name}, department : {employee.department}")
        else:
            print("\nUsers list is not available ")

    def remove_employee(self, employee_id):
        for employee in self.total_employees:
            if employee[1].employee_id == employee_id:
                self.total_employees.remove(employee)

emp_manager = Employee_manager()

while True:
    try:
        print("enter 1 : to add employees")
        print("enter 2 : show all the employees")
        print("enter 3 : Find an employee with respect to name or salary or birthday or area")
        print("Enter 4 : Quit")

        key1_pressed = int(input("Enter the number of operation you want to perform : "))
        if key1_pressed == 1:
            name = input("ENter your name : ")
            dob = input("Enter your birthdate in dd-mm-yyyy format : ")
            city = input("Enter your city : ")
            contact_no = int(input("ENter your contact number : "))
            joining_date = input("Enter your joining date in dd-mm-yyyy format : ")
            salary = int(input("Enter your salary"))
            department = input("Enter your department")
            post = input("Enter your post")

            Emp = Employee(name,dob,city,contact_no,joining_date,salary, department, post)
            emp_manager.total_employees.append(Emp)

            print("Employee added successfully !!!")

        elif key1_pressed == 2:
            emp_manager.show_employees()
        
        elif key1_pressed == 3:
            while True:
                print("Enter 1 : to find an employee with the name")
                print("ENter 2 : to find all employees with department Finance")
                print("Enter 3 : to find all employees whose salary is greater than 50000")
                print("Enter 4 : to find all employees whose salary is between 50000-100000")
                print("ENter 5 : Find a list of employees who are joined in the current year")
                print("Enter 6 : Find all employees who are from Mirzapur")
                print("ENter 7 : Find employees whose birthday in the current month")
                print("Enter 8 : Sort employee list with salary in descending order")
                print("Enter 9 : Quit")

                key2_pressed = int(input("Enter the number of the operation you want to perform"))
                if key2_pressed == 1:
                    name_of_employee = input("Enter the name of employee :")
                    for employee in emp_manager.total_employees:
                        if employee.name == name_of_employee:
                            print(f"Employee name : {employee.name}, Employee id :{employee.employee_id},employee department : {employee.department}, employe post : {employee.post}")
                        else:
                            print("No such an Employee is existed")

                elif key2_pressed == 2:
                    for employee in emp_manager.total_employees:
                        if employee.name == name_of_employee:
                            print(f"Employee name : {employee.name}, Employee id :{employee.employee_id},employee department : {employee.department}, employe post : {employee.post}")
                        else:
                            print("No such an Employee is existed")
                elif key2_pressed == 3:
                    for employee in emp_manager.total_employees:
                        if employee.name == name_of_employee:
                            print(f"Employee name : {employee.name}, Employee id :{employee.employee_id},employee department : {employee.department}, employe post : {employee.post}")
                        else:
                            print("No such an Employee is existed")
                elif key2_pressed == 4:
                    for employee in emp_manager.total_employees:
                        if employee.name == name_of_employee:
                            print(f"Employee name : {employee.name}, Employee id :{employee.employee_id},employee department : {employee.department}, employe post : {employee.post}")
                        else:
                            print("No such an Employee is existed")
                elif key2_pressed == 5:
                    for employee in emp_manager.total_employees:
                        if employee.name == name_of_employee:
                            print(f"Employee name : {employee.name}, Employee id :{employee.employee_id},employee department : {employee.department}, employe post : {employee.post}")
                        else:
                            print("No such an Employee is existed")
                elif key2_pressed == 6:
                    for employee in emp_manager.total_employees:
                        if employee.name == name_of_employee:
                            print(f"Employee name : {employee.name}, Employee id :{employee.employee_id},employee department : {employee.department}, employe post : {employee.post}")
                        else:
                            print("No such an Employee is existed")

                elif key2_pressed == 7:
                    for employee in emp_manager.total_employees:
                        if employee.name == name_of_employee:
                            print(f"Employee name : {employee.name}, Employee id :{employee.employee_id},employee department : {employee.department}, employe post : {employee.post}")
                        else:
                            print("No such an Employee is existed")

                elif key2_pressed == 8:
                    emp_manager.total_employees.sort(key = lambda x:x.salary, reverse = True)
                    for i in emp_manager.total_employees:
                        print(i.employee_id)

                elif key2_pressed == 9:
                    break
        elif key1_pressed == 4:
            break
    except Exception as e:
        print("Enter a valid value !!!",type(e).__name__,e)
        print_exc()

















