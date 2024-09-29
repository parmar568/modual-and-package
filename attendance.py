

attendance_records = {}

def mark_attendance(employee_id, status):
    """Mark the attendance of an employee."""
    attendance_records[employee_id] = status

def check_attendance(employee_id):
    """Check the attendance status of an employee."""
    return attendance_records.get(employee_id, "No record found")
