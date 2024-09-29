

from employee_attendance.attendance import mark_attendance, check_attendance
from employee_attendance.employee import add_employee, get_employee_details
from employee_attendance.utils import get_employee_input

employees = {}  
def main():
    while True:
        choice = input("Choice '1' to add employee\nChoice '2' to mark attendance\nChoice '3' to check attendance\nChoice '4' to exit\n Enter the choice:- ")

        if choice == '1':
            employee_id, name = get_employee_input()
            if employee_id and name:  
                employees[employee_id] = name  
                add_employee(employee_id, name) 
                print("Employee added!\n", end=" ")

        elif choice == '2':
            employee_id = input("Enter Employee ID to mark attendance: ")
            status = input("Enter status (P/A): ").strip().lower()
            if employee_id in employees:
                mark_attendance(employee_id, status)
                print("Attendance marked!\n", end=" ")
            else:
                print("Employee not found!")

        elif choice == '3':
            employee_id = input("Enter Employee ID to check attendance: ")
            if employee_id in employees:
                status = check_attendance(employee_id)
                print(f"Attendance for {employee_id}: {status}")
            else:
                print("Employee not found!")

        elif choice == '4':
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
