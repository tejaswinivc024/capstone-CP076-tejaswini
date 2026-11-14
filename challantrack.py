
from modules.offence_management import add_offence, view_offences
from modules.challan_management import generate_challan
from modules.payment_management import record_payment
from modules.reports import (
    view_all_challans,
    view_pending_challans,
    view_vehicle_dues
)
from modules.licence_management import add_licence, check_licence_status
from modules.area_reports import generate_area_report


def display_menu():
    print("\n========================================")
    print("             CHALLANTRACK")
    print(" Traffic Violation and Penalty Management")
    print("========================================")
    print("1. Offence Management")
    print("2. Generate Challan")
    print("3. View All Challans")
    print("4. Record Challan Payment")
    print("5. View Pending Challans")
    print("6. View Vehicle Pending Dues")
    print("7. Driving Licence Management")
    print("8. Area-wise Offence Report")
    print("9. Exit")
    print("========================================")


def offence_menu():
    while True:
        print("\n-------- OFFENCE MANAGEMENT --------")
        print("1. Add Offence")
        print("2. View Offences")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_offence()

        elif choice == "2":
            view_offences()

        elif choice == "3":
            break

        else:
            print("Invalid choice! Please try again.")


def licence_menu():
    while True:
        print("\n------ DRIVING LICENCE MANAGEMENT ------")
        print("1. Register Driving Licence")
        print("2. Check Licence Status")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_licence()

        elif choice == "2":
            licence_number = input("Enter driving licence number: ").strip().upper()
            check_licence_status(licence_number)

        elif choice == "3":
            break

        else:
            print("Invalid choice! Please try again.")


def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            offence_menu()

        elif choice == "2":
            generate_challan()

        elif choice == "3":
            view_all_challans()

        elif choice == "4":
            record_payment()

        elif choice == "5":
            view_pending_challans()

        elif choice == "6":
            view_vehicle_dues()

        elif choice == "7":
            licence_menu()

        elif choice == "8":
            generate_area_report()

        elif choice == "9":
            print("\nThank you for using ChallanTrack!")
            break

        else:
            print("\nInvalid choice! Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()
