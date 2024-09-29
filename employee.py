

employees = {}

def add_employee(employee_id, name):
    """Add a new employee."""
    employees[employee_id] = name

def get_employee_details(employee_id):
    """Get the details of an employee."""
    return employees.get(employee_id, "Employee not found")
