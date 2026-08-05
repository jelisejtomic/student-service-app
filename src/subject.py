import data_handler


def display_subjects(subjects_list):
    """Prints a formatted table of subjects."""
    if not subjects_list:
        print("No subjects to display.")
        return

    print("No.\tSubject ID\tSubject Name")
    print("-" * 60)
    i = 0
    for subject in subjects_list:
        i += 1
        print(f"{i}.\t{subject['subject_id']}\t\t{subject['subject_name']}")
    print("-" * 60)


def display_subjects_by_codes(subject_ids):
    """Displays specific subjects matching provided ID list."""
    if not subject_ids:
        print("No subjects found matching the specified criteria.")
        return

    subjects = data_handler.load_subjects()
    found = False

    for subj in subjects:
        if str(subj["subject_id"]) in subject_ids:
            found = True
            print(f"ID: {subj['subject_id']} | Name: {subj['subject_name']}")

    if not found:
        print("No subjects found matching the specified criteria.")


def display_passed_subjects_with_grades(passed_grades_map):
    """Displays passed subjects along with the obtained grades."""
    if not passed_grades_map:
        print("No passed subjects found.")
        return

    subjects = data_handler.load_subjects()
    found = False

    print(f"{'ID':<5} | Subject Name (Grade)")
    print("-" * 60)
    for subj in subjects:
        subj_id_str = str(subj["subject_id"])
        if subj_id_str in passed_grades_map:
            found = True
            grade = passed_grades_map[subj_id_str]
            print(f"{subj['subject_id']:<5} | {subj['subject_name']} ({grade})")

    if not found:
        print("No passed subjects found.")
