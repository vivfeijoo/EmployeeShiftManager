from database import create_tables
from shift_manager import add_shift, view_shifts, edit_shift, delete_shift

def menu():
    create_tables()
    while True:
        print("\n1. Add Shift\n2. View Shifts\n3. Edit Shift\n4. Delete Shift\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Employee name: ")
            date = input("Shift date (YYYY-MM-DD): ")
            shift_type = input("Shift type (Morning/Afternoon/Night): ")
            add_shift(name, date, shift_type)

        elif choice == "2":
            view_shifts()

        elif choice == "3":
            shift_id = input("Shift ID to edit: ")
            new_name = input("New employee name: ")
            new_date = input("New shift date (YYYY-MM-DD): ")
            new_type = input("New shift type (Morning/Afternoon/Night): ")
            edit_shift(shift_id, new_name, new_date, new_type)

        elif choice == "4":
            shift_id = input("Shift ID to delete: ")
            delete_shift(shift_id)

        elif choice == "5":
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()
