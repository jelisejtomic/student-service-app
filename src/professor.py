import data_handler
import utils


def display_professors(professors_list):
    """Prints details of professors passed in the list."""
    if not professors_list:
        print("No professors to display.")
        return

    for prof in professors_list:
        print("---".center(60))
        print(f"Name: {prof['first_name']} {prof['last_name']}")
        print(f"Email: {prof['email']}")
        print(f"Consultations: {prof['consultations']}")


# --- Helper functions ---
def _search_students_by_name(students):
    """Searches students by first name and displays matching results."""
    search_name = input("Enter student first name: ").strip().lower()

    matching_students = []
    for s in students:
        if search_name in str(s["first_name"]).lower():
            matching_students.append(s)

    if not matching_students:
        print("-" * 60)
        print(f"No students were found whose name contains '{search_name}'.")
        return None

    print("--- Students Found ---")
    for s in matching_students:
        print(f"ID: {s['student_id']} | Name: {s['first_name']} {s['last_name']}")
    print("-" * 60)

    return matching_students


def _select_student_by_id(students):
    """Prompts professor to choose a student by ID from the matching list."""
    while True:
        student_id_input = utils.read_int("Enter Student ID: ")
        for student in students:
            if student["student_id"] == student_id_input:
                return student
        print("Student not found in the search results! Try again.")
        print("-" * 60)


def _select_subject_by_id(subjects):
    """Displays available subjects and prompts selection by ID."""
    print("--- Available Subjects ---")
    for subj in subjects:
        print(f"ID: {subj['subject_id']} | Name: {subj['subject_name']}")
    print("-" * 60)

    while True:
        subject_id_input = utils.read_int("Enter Subject ID: ")

        for subj in subjects:
            if subj["subject_id"] == subject_id_input:
                return subject_id_input

        print("Subject with this ID does not exist! Try again.")
        print("-" * 60)


# --- Main Feature Functions ---
def add_grade(professor_id):
    """Adds a grade for a student in a specific subject."""
    students = data_handler.load_students()
    subjects = data_handler.load_subjects()

    if not students:
        print("The system does not contain data on students.")
        return

    # Search student by first name
    matching_students = _search_students_by_name(students)
    if not matching_students:
        return

    # Select student by ID
    selected_student = _select_student_by_id(students)

    # Select subject by ID
    subject_id_input = _select_subject_by_id(subjects)

    # Grade validation (5–10)
    while True:
        grade_input = utils.read_int("Enter grade (5-10): ")
        if 5 <= grade_input <= 10:
            break
        else:
            print("Grade must be in the range between 5 and 10! Try again.")
            print("-" * 60)

    # Update and save data
    new_grade = {
        "subject_id": str(subject_id_input),
        "professor_id": str(professor_id),
        "grade": grade_input,
    }

    if "grades" not in selected_student:
        selected_student["grades"] = []

    selected_student["grades"].append(new_grade)

    data_handler.save_students(students)
    print("-" * 60)
    print(
        f"Successfully added grade ({grade_input}) for student {selected_student['first_name']} {selected_student['last_name']}!"
    )


def delete_grade(professor_id):
    """Deletes a grade for a student assigned by the logged-in professor."""
    students = data_handler.load_students()

    if not students:
        print("The system does not contain data on students.")
        return

    # Search student by first name
    matching_students = _search_students_by_name(students)
    if not matching_students:
        return

    # Select student by ID
    selected_student = _select_student_by_id(matching_students)

    # Display only grades assigned by the logged-in professor
    student_grades = selected_student["grades"]
    prof_grades = []

    for item in student_grades:
        if str(item["professor_id"]) == str(professor_id):
            prof_grades.append(item)

    if not prof_grades:
        print("-" * 60)
        print("No grades found for this student that were assigned by you.")
        return

    print(f"--- Grades assigned by Professor (ID: {professor_id}) ---")
    print(f"{'#':<3} | {'Subject ID':<10} | {'Grade':<5}")
    print("-" * 30)
    i = 1
    for g in prof_grades:
        print(f"{i:<3} | {g['subject_id']:<10} | {g['grade']:<5}")
        i += 1
    print("-" * 60)

    # Select grade by ordinal number and remove it
    while True:
        no_input = utils.read_int("Enter grade # to delete (0 to cancel): ")
        if no_input == 0:
            print("-" * 60)
            print("Operation canceled.")
            break
        if 1 <= no_input <= len(prof_grades):
            grade_to_remove = prof_grades[no_input - 1]
            selected_student["grades"].remove(grade_to_remove)
            # i = 0
            # for g in selected_student["grades"]:
            #     if g is grade_to_remove:
            #         del selected_student["grades"][i]
            #         break
            #     i += 1
            data_handler.save_students(students)
            print("-" * 60)
            print(
                f"Successfully deleted grade ({grade_to_remove['grade']}) for subject ID '{grade_to_remove['subject_id']}'."
            )
            break
        else:
            if len(prof_grades) > 2:
                print(
                    f"Invalid option! Number must be in range between 1 and {len(prof_grades)} (or 0 to cancel)."
                )
            else:
                print("Invalid option! Please enter a number 1 or 2 (or 0 to cancel).")
            print("-" * 60)


def calculate_subject_gpa(professor_id):
    """Calculates average grade for a specific subject taught by the logged-in professor."""
    subjects = data_handler.load_subjects()
    students = data_handler.load_students()

    if not subjects:
        print("The system does not contain data on subjects.")
        return

    if not students:
        print("The system does not contain data on students.")
        return

    # Select subject from the available list
    selected_subject_id = _select_subject_by_id(subjects)

    # Find selected subject name for cleaner output
    subject_name = ""
    for subj in subjects:
        if str(subj["subject_id"]) == str(selected_subject_id):
            subject_name = subj["subject_name"]
            break

    # Find all grades matching the selected subject and logged-in professor
    matching_grades = []
    for student in students:
        for item in student["grades"]:
            if (
                str(item["subject_id"]) == str(selected_subject_id)
                and str(item["professor_id"]) == str(professor_id)
                and "grade" in item
            ):
                matching_grades.append(item["grade"])

    # Calculate and display average GPA or notice if no grades exist
    print("-" * 60)
    if not matching_grades:

        print(f"No grades found for subject '{subject_name}' assigned by you.")
        return

    average_gpa = sum(matching_grades) / len(matching_grades)
    print(
        f"Average GPA for '{subject_name}' (ID: {selected_subject_id}): {round(average_gpa, 2)}"
    )
    print(f"Total grades analyzed: {len(matching_grades)}")


def update_consultation_hours(professor_id):
    """Updates consultation hours for the logged-in professor."""
    professors = data_handler.load_professors()
    for prof in professors:
        if prof["professor_id"] == professor_id:
            while True:
                print(f"Current Consultations: {prof['consultations']}")
                new_schedule = input(
                    "Enter new schedule (Leave empty to keep current): "
                ).strip()
                if not new_schedule:
                    print("-" * 60)
                    print("No changes made.")
                    return

                if len(new_schedule) > 8 and "," in new_schedule:
                    prof["consultations"] = new_schedule
                    data_handler.save_professors(professors)
                    print("-" * 60)
                    print("Consultation hours updated successfully!")
                    return
                else:
                    print("Invalid input! Enter schedule in format 'day, hour-hour'.")
                    print("-" * 60)


def professor_menu(professor):
    professor_id = professor["professor_id"]
    while True:
        print("=" * 60)
        print("--- Professor Menu ---".center(60))
        print("-" * 60)
        print("1. Add Grade to Student")
        print("2. Delete Grade from Student")
        print("3. Calculate Subject Average GPA")
        print("4. Update Consultation Schedule")
        print("5. Return to Main Menu")
        print("-" * 60)
        option = input("Select an option (1-5): ").strip()
        print("-" * 60)

        if option == "1":
            add_grade(professor_id)
        elif option == "2":
            delete_grade(professor_id)
        elif option == "3":
            calculate_subject_gpa(professor_id)
        elif option == "4":
            update_consultation_hours(professor_id)
        elif option == "5":
            print("Back to Main Menu")
            break
        else:
            print("Invalid option! Please select a number between 1 and 5.")
