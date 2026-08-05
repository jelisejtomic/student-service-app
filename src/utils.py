def read_int(prompt):
    """Safely prompts user for an integer until valid input is given."""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            print("-" * 60)
