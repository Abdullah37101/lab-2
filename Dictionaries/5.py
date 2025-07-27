def main():
    employees = {}

    add_employee(employees, 101, "Alice Johnson", "Manager", 75000)
    add_employee(employees, 102, "Bob Smith", "Developer", 60000)
    add_employee(employees, 103, "Carol White", "Designer", 55000)

    for emp_id, info in employees.items():
        print(f"Employee #{emp_id}:")
        for key, value in info.items():
            print(f"  {key}: {value}")
        print()


def add_employee(employees, emp_number, name, position, salary):
        employees[emp_number] = {
            "Name": name,
            "Position": position,
            "Salary": salary
        }


if __name__ == "__main__":
    main()