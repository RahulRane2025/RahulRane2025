employees = {
    101: {"Name": "Satya", "Age": 27, "Department": "HR", "Salary": 50000},
    102: {"Name": "Ravi", "Age": 30, "Department": "Finance", "Salary": 60000},
    103: {"Name": "Neha", "Age": 25, "Department": "IT", "Salary": 55000}
         }

def main_menu():
    #Display Main menu & Necessary function based on user input.
    while True:
        print("!!**********************************!!\n")
        print("\n---Employee Management System(EMS)---")
        print("\n!!**********************************!!")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
       
        choice = input("Enter Your Choice: ")
        if choice == "1":
            Add_Employee()
        elif choice == "2":
            View_Employees()
        elif choice == "3":
            Search_Employee()
        elif choice == "4":
            print("Thank you for using the Employee Management System(EMS).")
            break
        else:
            print("Invalid Choice! Please select a valid option.")

def Add_Employee():
    '''Add New employee- dictionary after validating input.'''
    print("!!**********************************!!")
    print("--- Add New Employee ---")
    print("!!**********************************!!")    
    Emp_id = int(input("Enter Employee ID:"))
    
    # Employee ID:unique
    if Emp_id in employees:
        print("Error: Employee ID already exists! Please Enter a unique ID")
        return
    Name = input("Enter Employee Name: ")
    Age = int(input("Enter Employee Age: "))
    Department = input("Enter Employee Department: ")
    Salary = float(input("Enter Employee Salary: "))
    
    # Store Employee Data
    employees[Emp_id] = {"Name":Name,"Age": Age, 'Department': Department, "Salary": Salary}
    print("!!=============================================\n!!")  
    print(f"Employee with ID {Emp_id} added successfully!")
    print("!!=============================================\n!!")  

def View_Employees():
    #Displays all employee Details in a Table format.
    print("\n**** View All Employees ***")
    if not employees:
        print("!!=====================!!\n")
        print("No Employees Available")
        print("!!=====================!!\n")
        return
    
    print(f"{'ID':<10}{'Name':<20}{'Age':<10}{'Department':<20}{'Salary':<10}")
    print("-" * 70)
    
    for Emp_id, details in employees.items():
        print(f"{Emp_id:<10}{details['Name']:<20}{details['Age']:<10}{details['Department']:<20}{details['Salary']:<10.2f}")
        
def Search_Employee():
    #Searches for an employee by their ID and displays their details.
    
    print("\n---Search for Employee---")
    
    Emp_id = int(input("Enter Employee ID to search: "))
    
    if Emp_id in employees:
        details = employees[Emp_id]
        print(f"Employee Found: ID: {Emp_id}, Name:{details['Name']}, Age:{details['Age']}, Department: {details['Department']}, Salary:{details['Salary']}")
    else:
        print("Employee Not Found.")

if __name__ == "__main__":
    main_menu()
