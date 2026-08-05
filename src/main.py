import auth


def main_menu():
    print("=" * 60)
    print("--- Student Service App ---".center(60))
    print("=" * 60)
    print("1. Login")
    print("2. Registration")
    print("3. Exit Application")
    print("=" * 60)
    return input("Select an option (1-3): ").strip()


def main():
    while True:
        choice = main_menu()
        if choice == "1":
            auth.login_menu()
        elif choice == "2":
            auth.registration_menu()
        elif choice == "3":
            print("-" * 60 + "\nGoodbye!")
            break
        else:
            print("-" * 60)
            print("Invalid option! Please select a number between 1 and 3.")


if __name__ == "__main__":
    main()
