# Student Service Console Application

A modular, CLI-based Student Service application built with Python for the _Principles of computer programming_ course. The application enables seamless interaction for both professors and students.

## Features

### Professor Role

- **Add Grade:** Search students by first name, select by id, choose a subject, and assign a grade.
- **Delete Grade:** View and remove grades previously assigned by the logged-in professor.
- **Calculate Subject GPA:** Compute the average grade for a selected subject taught by the professor.
- **Update Consultations:** Update consultation hours with input validation.

### Student Role

- **Calculate Overall GPA:** Compute and display the cumulative GPA across all passed subjects.
- **View Passed & Unpassed Subjects:** Filter and review academic performance by subject status.
- **Find Subject Professor:** View assigned professors and their office hours for any chosen subject.

## Requirements & Setup

### Prerequisites

- **Python Version**: 3.8 or higher

### Running the Application

1. **Clone the Repository**

    ```bash
    git clone https://github.com/jelisejtomic/student-service-app.git
    cd student-service-app
    ```

2. **Run the application**
    ```bash
    python src/main.py
    ```

## Technical Highlights

- **Modular Architecture:** Clean separation of concerns across data handling, authentication, role-specific logic, and utility functions.
- **Data Storage:** Custom-parsed CSV format (UTF-8 encoded) for subjects and professors, paired with JSON storage for nested student records.
- **Robust Error Handling:** Crash-resistant input loops using standard try-except blocks to handle invalid inputs gracefully (ValueError, FileNotFoundError, etc.).
- **UTF-8 Encoding:** Full support for international character sets across all file read/write operations.
