import data_handler
import subject
import professor
import utils


def calculate_gpa(student_id):
    """Calculates overall average grade for a logged-in student."""
    students = data_handler.load_students()
    all_grades = []

    for s in students:
        if s["student_id"] == student_id:
            for item in s["grades"]:
                if "grade" in item:
                    all_grades.append(item["grade"])

            if len(all_grades) > 0:
                avg = sum(all_grades) / len(all_grades)
                print(f"Overall GPA: {round(avg, 2)}")
                print(f"Total grades analyzed: {len(all_grades)}")
            else:
                print("No grades registered for this student.")
            return
    print("Student not found.")


def display_passed_unpassed_subjects(student_id):
    """Displays passed or failed subjects based on student selection."""
    students = data_handler.load_students()
    subjects = data_handler.load_subjects()

    target_student = None
    for s in students:
        if s["student_id"] == student_id:
            target_student = s
            break

    if not target_student:
        print("Student record not found.")
        return

    while True:
        print("1. Passed Subjects\n2. Unpassed Subjects")
        print("-" * 60)
        option = input("Select an option (1|2): ").strip()
        print("-" * 60)

        # passed_codes = []
        passed_grades_map = {}
        for item in target_student["grades"]:
            if "grade" in item:
                # passed_codes.append(str(item["subject_id"]))
                passed_grades_map[str(item["subject_id"])] = item["grade"]

        if option == "1":
            print("--- Passed Subjects ---")
            # subject.display_subjects_by_codes(passed_codes)
            subject.display_passed_subjects_with_grades(passed_grades_map)
            break
        elif option == "2":
            print("--- Unpassed Subjects ---")
            unpassed_codes = []
            for s in subjects:
                if str(s["subject_id"]) not in passed_grades_map:
                    unpassed_codes.append(str(s["subject_id"]))
            subject.display_subjects_by_codes(unpassed_codes)
            break
        else:
            print("Invalid option! Please select 1 or 2.")


def display_subject_professor():
    """Displays professor details for a selected subject by checking student grades."""
    subjects = data_handler.load_subjects()

    # Display all subjects
    subject.display_subjects(subjects)

    while True:
        subject_id_input = utils.read_int("Enter Subject ID: ")

        target_subject = None
        for sub in subjects:
            if sub["subject_id"] == subject_id_input:
                target_subject = sub
                break

        if not target_subject:
            print("Subject with this ID does not exist! Try again.")
            print("-" * 60)
        else:
            break

    # Search through students and their grades
    students = data_handler.load_students()
    professor_ids = set()

    for stud in students:
        for item in stud["grades"]:
            if item["subject_id"] == str(subject_id_input) and "professor_id" in item:
                professor_ids.add(str(item["professor_id"]))

    if not professor_ids:
        print(f"No professor teaches '{target_subject['subject_name']}' subject.")
        return

    # Filter and display professors
    professors = data_handler.load_professors()
    matched_professors = []

    for prof in professors:
        if str(prof["professor_id"]) in professor_ids:
            matched_professors.append(prof)

    if matched_professors:
        print(f"Professors teaching '{target_subject['subject_name']}' subject:")
        professor.display_professors(matched_professors)
    else:
        print(f"No professor teaches '{target_subject['subject_name']}' subject.")


def student_menu(student):
    student_id = student["student_id"]
    while True:
        print("=" * 60)
        print("--- Student Menu ---".center(60))
        print("-" * 60)
        print("1. Calculate Overall GPA")
        print("2. View Passed / Unpassed Subjects")
        print("3. View Subject Professor Details")
        print("4. Return to Main Menu")
        print("-" * 60)
        option = input("Select an option (1-4): ").strip()
        print("-" * 60)

        if option == "1":
            calculate_gpa(student_id)
        elif option == "2":
            display_passed_unpassed_subjects(student_id)
        elif option == "3":
            display_subject_professor()
        elif option == "4":
            print("Back to Main Menu")
            break
        else:
            print("-" * 60)
            print("Invalid option! Please select a number between 1 and 4.")
