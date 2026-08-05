import json
import os

SUBJECTS_FILE = "student-service-app/data/subjects.csv"
PROFESSORS_FILE = "student-service-app/data/professors.csv"
STUDENTS_FILE = "student-service-app/data/students.json"


def load_subjects():
    subjects = []
    try:
        with open(SUBJECTS_FILE, mode="r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(";")
                if len(parts) >= 2:
                    subject = {
                        "subject_id": int(parts[0]),
                        "subject_name": parts[1],
                    }
                    subjects.append(subject)
    except FileNotFoundError:
        print(f"Error: File {SUBJECTS_FILE} not found.")
    return subjects


def save_subjects(subjects):
    try:
        with open(SUBJECTS_FILE, mode="w", encoding="utf-8") as file:
            for sub in subjects:
                line = f"{sub['subject_id']};{sub['subject_name']}\n"
                file.write(line)
    except Exception as e:
        print(f"Unexpected error while saving subject data: {e}")


def load_professors():
    professors = []
    try:
        with open(PROFESSORS_FILE, mode="r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("-")
                if len(parts) >= 6:
                    professor = {
                        "professor_id": int(parts[0]),
                        "password": parts[1],
                        "first_name": parts[2],
                        "last_name": parts[3],
                        "email": parts[4],
                        "consultations": "-".join(parts[5:]),
                    }
                    professors.append(professor)
    except FileNotFoundError:
        print(f"Error: File {PROFESSORS_FILE} not found.")
    return professors


def save_professors(professors):
    try:
        with open(PROFESSORS_FILE, mode="w", encoding="utf-8") as file:
            for prof in professors:
                line = f"{prof['professor_id']}-{prof['password']}-{prof['first_name']}-{prof['last_name']}-{prof['email']}-{prof['consultations']}\n"
                file.write(line)
    except Exception as e:
        print(f"Unexpected error while saving professor data: {e}")


def load_students():
    if not os.path.exists(STUDENTS_FILE):
        return []
    try:
        with open(STUDENTS_FILE, mode="r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Unexpected error while reading file: {e}")
        return []


def save_students(students):
    try:
        with open(STUDENTS_FILE, mode="w", encoding="utf-8") as file:
            json.dump(students, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Unexpected error while saving data: {e}")
