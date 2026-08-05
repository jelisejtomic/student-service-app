import data_handler
import utils


def register_professor():
    """Registers a new professor with unique ID validation."""
    professors = data_handler.load_professors()

    while True:
        input_id = utils.read_int("Enter professor ID: ")
        exists = False
        for p in professors:
            if p["professor_id"] == input_id:
                exists = True
                break
        if exists:
            print("Professor with this ID already exists! Try again.")
            print("-" * 60)
        else:
            break

    password = input("Enter password: ").strip()
    first_name = input("Enter first name: ").strip()
    last_name = input("Enter last name: ").strip()
    email = input("Enter email: ").strip()

    while True:
        consultations = input(
            "Enter consultation time (e.g. Tuesday, 10-11 am): "
        ).strip()
        if len(consultations) > 8 or "," in consultations:
            break
        else:
            print("Invalid input! Format must be 'day, hour-hour'.")
            print("-" * 60)

    new_prof = {
        "professor_id": input_id,
        "password": password,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "consultations": consultations,
    }

    professors.append(new_prof)
    data_handler.save_professors(professors)
    print("-" * 60)
    print("Professor registered successfully!")


def register_student():
    """Registers a new student with unique ID validation."""
    students = data_handler.load_students()

    while True:
        input_id = utils.read_int("Enter Student ID: ")
        exists = False
        for st in students:
            if st["student_id"] == input_id:
                exists = True
                break
        if exists:
            print("Student with this ID already exists! Try again.")
            print("-" * 60)
        else:
            break

    password = input("Enter password: ").strip()
    first_name = input("Enter first name: ").strip()
    last_name = input("Enter last name: ").strip()
    email = input("Enter email: ").strip()

    new_student = {
        "student_id": input_id,
        "password": password,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "grades": [],
    }

    students.append(new_student)
    data_handler.save_students(students)
    print("-" * 60)
    print("Student registered successfully!")


def login():
    """
    Authenticates user (professor or student).
    Returns a tuple: (user_object, user_role) or (None, None) if login fails.
    user_role can be 'professor' or 'student'.
    """
    user_id = input("Enter ID: ").strip()
    password = input("Enter Password: ").strip()
    print("-" * 60)

    # Check professors first
    professors = data_handler.load_professors()
    for prof in professors:
        if str(prof["professor_id"]) == user_id and prof["password"] == password:
            print(f"Welcome, Prof. {prof['first_name']} {prof['last_name']}!")
            return prof, "professor"

    # Check students
    students = data_handler.load_students()
    for st in students:
        if str(st["student_id"]) == user_id and st["password"] == password:
            print(f"Welcome, {st['first_name']} {st['last_name']}!")
            return st, "student"

    print("Invalid credentials! Try again.")
    return None, None


def login_menu():
    print("=" * 60)
    user, role = login()
    if user:
        if role == "professor":
            import professor

            professor.professor_menu(user)
        elif role == "student":
            import student

            student.student_menu(user)


def registration_menu():
    while True:
        print("=" * 60)
        print("Register as:\n1. Professor\n2. Student\n3. Return to Main Menu")
        print("-" * 60)
        option = input("Select an option (1-3): ").strip()
        print("-" * 60)
        if option == "1":
            register_professor()
            break
        elif option == "2":
            register_student()
            break
        elif option == "3":
            print("Back to Main Menu")
            break
        else:
            print("Invalid option! Please select a number between 1 and 3.")
