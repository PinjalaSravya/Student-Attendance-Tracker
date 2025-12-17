from datetime import date

FILE_NAME = "attendance.txt"


def add_student(students):
    roll = input("Enter roll number: ").strip()
    name = input("Enter student name: ").strip()

    if roll in students:
        print("Student already exists.")
        return

    students[roll] = name
    print("Student added successfully.")


def mark_attendance(students):
    if not students:
        print("No students available.")
        return

    today = date.today().isoformat()

    with open(FILE_NAME, "a") as file:
        file.write(f"\nDate: {today}\n")

        print("\nMark Attendance (P/A):")
        for roll, name in students.items():
            status = input(f"{roll} {name}: ").strip().upper()

            if status not in ["P", "A"]:
                status = "A"

            status_word = "Present" if status == "P" else "Absent"
            file.write(f"{roll} {name} {status_word}\n")

    print("Attendance marked successfully.")


def view_attendance():
    try:
        with open(FILE_NAME, "r") as file:
            print("\n--- ATTENDANCE RECORDS ---")
            print(file.read())
    except FileNotFoundError:
        print("No attendance records found.")


def main():
    students = {}

    while True:
        print("\n--- STUDENT ATTENDANCE TRACKER ---")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance Records")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            mark_attendance(students)
        elif choice == "3":
            view_attendance()
        elif choice == "4":
            print("Exiting Attendance Tracker.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
