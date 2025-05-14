from database import create_tables
from shift_manager import add_shift, view_shifts

def menu():
    create_tables()
    while True:
        print("\n1. Add Shift\n2. View Shifts\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Employee name: ")
            date = input("Shift date (YYYY-MM-DD): ")
            shift_type = input("Shift type (Morning/Afternoon/Night): ")
            add_shift(name, date, shift_type)
        elif choice == "2":
            view_shifts()
        elif choice == "3":
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()
