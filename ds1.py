# Sample initial employee data
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Anita', 'age': 30, 'department': 'Finance', 'salary': 60000}
}

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search for Employee")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == '1':
        # Add Employee
        print("\n--- Add Employee ---")
        while True:
            try:
                emp_id = int(input("Enter Employee ID (unique integer): ").strip())
            except ValueError:
                print("Invalid input! Employee ID must be an integer.")
                continue

            if emp_id in employees:
                print(f"Employee ID {emp_id} already exists. Please enter a unique Employee ID.")
            else:
                break

        name = input("Enter Employee Name: ").strip()

        while True:
            try:
                age = int(input("Enter Employee Age: ").strip())
                if age <= 0:
                    print("Age must be positive.")
                    continue
                break
            except ValueError:
                print("Invalid input! Age must be an integer.")

        department = input("Enter Employee Department: ").strip()

        while True:
            try:
                salary = float(input("Enter Employee Salary: ").strip())
                if salary < 0:
                    print("Salary cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid input! Salary must be a number.")

        employees[emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }

        print(f"Employee {name} (ID: {emp_id}) successfully added.")

    elif choice == '2':
        # View All Employees
        print("\n--- All Employees ---")
        if not employees:
            print("No employees available.")
        else:
            print(f"{'ID':<8}{'Name':<20}{'Age':<6}{'Department':<15}{'Salary':<10}")
            print("-" * 60)
            for emp_id, data in employees.items():
                print(f"{emp_id:<8}{data['name']:<20}{data['age']:<6}{data['department']:<15}{data['salary']:<10.2f}")

    elif choice == '3':
        # Search for Employee
        print("\n--- Search Employee ---")
        try:
            emp_id = int(input("Enter Employee ID to search: ").strip())
        except ValueError:
            print("Invalid input! Employee ID must be an integer.")
            continue

        if emp_id in employees:
            data = employees[emp_id]
            print(f"\nDetails for Employee ID {emp_id}:")
            print(f"Name      : {data['name']}")
            print(f"Age       : {data['age']}")
            print(f"Department: {data['department']}")
            print(f"Salary    : {data['salary']:.2f}")
        else:
            print("Employee not found.")

    elif choice == '4':
        print("Thank you for using the Employee Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
