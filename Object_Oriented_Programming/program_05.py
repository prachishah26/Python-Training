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

class EmployeeManager():
    def __init__(self):
        self.total_employees = []
    def show_employees(self):
        if len(self.total_employees) != 0:
            for employee in self.total_employees:
                print(f"\nEmployee id : {employee.employee_id}, Name of employee : {employee.name}, department : {employee.department}")
        else:
            print("\nUsers list is not available ")

    def remove_employee(self, employee_id):
        for employee in self.total_employees:
            if employee.employee_id == employee_id:
                self.total_employees.remove(employee)

emp_manager = EmployeeManager()
print("\nWelcome !")
while True:
    try:
        
        print("\nenter 1 : To add employees")
        print("enter 2 : Show all the employees")
        print("enter 3 : Find an employee with respect to name or salary or birthday or area")
        print("enter 4 : To remove user")
        print("Enter 5 : Quit\n")

        key1_pressed = int(input("Enter the number of operation you want to perform : "))
        if key1_pressed > 5:
            print("\nPLease enter number from 1 to 5.")
        if key1_pressed == 1:
            name = input("\nEnter your name : ")
            dob = input("Enter your birthdate in dd-mm-yyyy format : ")
            city = input("Enter your city : ")
            contact_no = int(input("Enter your contact number : "))
            joining_date = input("Enter your joining date in dd-mm-yyyy format : ")
            salary = int(input("Enter your salary : "))
            department = input("Enter your department : ")
            post = input("Enter your post : ")

            Emp = Employee(name,dob,city,contact_no,joining_date,salary, department, post)
            emp_manager.total_employees.append(Emp)

            print("\nEmployee added successfully !!!")

        elif key1_pressed == 2:
            emp_manager.show_employees()
        
        elif key1_pressed == 3:
            while True:
                print("\nEnter 1 : To find an employee with the name")
                print("ENter 2 : To find all employees with department Finance")
                print("Enter 3 : To find all employees whose salary is greater than 50000")
                print("Enter 4 : To find all employees whose salary is between 50000-100000")
                print("ENter 5 : Find a list of employees who are joined in the current year")
                print("Enter 6 : Find all employees who are from Mirzapur")
                print("ENter 7 : Find employees whose birthday in the current month")
                print("Enter 8 : Sort employee list with salary in descending order")
                print("Enter 9 : Back\n")

                key2_pressed = int(input("Enter the number of the operation you want to perform : "))
                if key2_pressed > 9:
                    print("\nPlease enter number between 1 to 9.")
                if key2_pressed == 1:
                    name_of_employee = input("\nEnter the name of employee :")
                    if len(emp_manager.total_employees) != 0:
                        for employee in emp_manager.total_employees:
                            if employee.name == name_of_employee:
                                print(f"\nEmployee name : {employee.name}, Employee id :{employee.employee_id},employee department : {employee.department}, employe post : {employee.post}\n")
                    else:
                        print("No such user existed !!!")

                elif key2_pressed == 2:
                    for employee in emp_manager.total_employees:
                        if employee.department == "fianance":
                            print(f"\nEmployee name : {employee.name}, Employee id :{employee.employee_id},employee department : {employee.department}, employe post : {employee.post}\n")
                        elif employee.department != "fianance":
                            pass
                        else:
                            print("\n------")

                elif key2_pressed == 3:
                    for employee in emp_manager.total_employees:
                        if employee.salary > 50000:
                            print(f"\nEmployee name : {employee.name}, Employee salary : {employee.salary} ,Employee id :{employee.employee_id},employee department : {employee.department}, employe post : {employee.post}\n")
                        elif employee.salary <= 50000 :
                            pass
                        else:
                            print("\nNo such an Employee is existed")

                elif key2_pressed == 4:
                    for employee in emp_manager.total_employees:
                        if employee.salary > 50000 and employee.salary < 100000:
                            print(f"\nEmployee name : {employee.name}, Employee salary : {employee.salary} ,Employee id :{employee.employee_id},employee department : {employee.department}, employe post : {employee.post}\n")
                        elif employee.salary <= 50000 and employee.salary >= 100000:
                            pass
                        else:
                            print("\nNo such an Employee is existed")

                elif key2_pressed == 5:
                    for employee in emp_manager.total_employees:
                        if employee.joining_date[-4:] == "2022":
                            print(f"\nEmployee name : {employee.name}, Employee id :{employee.employee_id},employee department : {employee.department}, employe post : {employee.post}\n")
                        elif employee.joining_date[-4:] != "2022":
                            pass
                        else:
                            print("\nNo such an Employee is existed")

                elif key2_pressed == 6:
                    for employee in emp_manager.total_employees:
                        if employee.city == "mirzapur":
                            print(f"\nEmployee name : {employee.name}, Employee id :{employee.employee_id},employee department : {employee.department}, employe post : {employee.post}\n")
                        elif employee.city != "mirzapur":
                            pass
                        else:
                            print("\nNo such an Employee is existed")

                elif key2_pressed == 7:
                    for employee in emp_manager.total_employees:
                        if employee.dob[3:5] == "03":
                            print(f"\nEmployee name : {employee.name}, Employee id :{employee.employee_id},employee department : {employee.department}, employe post : {employee.post}\n")
                        elif employee.dob[3:5] != "03":
                            pass
                        else:
                            print("\nNo such an Employee is existed")

                elif key2_pressed == 8:
                    emp_manager.total_employees.sort(key = lambda x:x.salary, reverse = True)
                    for employee in emp_manager.total_employees:
                        print(f"\nemployee id : {employee.employee_id},Employee salary : {employee.salary}, Employee name : {employee.name}, Employee department : {employee.department}, employee post : {employee.post} \n")

                elif key2_pressed == 9:
                    break

        elif key1_pressed == 4:
            emp_id = int(input("Enter the employee id : "))
            emp_manager.remove_employee(emp_id)
            print("\nEmployee is removed !")

        elif key1_pressed == 5:
            print("\nSee you again :) ")
            break

    except:
        print("Enter a valid value !!!")
        # print_exc()

 















