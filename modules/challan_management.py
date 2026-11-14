
from datetime import date
from modules.storage import load_data, save_data
from modules.vehicle_validation import validate_vehicle_number
from modules.licence_management import check_licence_status


def generate_challan():
    vehicle_number = input("Enter vehicle number: ").strip().upper()

    if not validate_vehicle_number(vehicle_number):
        print("Invalid vehicle number!")
        return

    licence_number = input("Enter driving licence number: ").strip().upper()

    licences = load_data("licences.json")

    licence_found = False

    for licence in licences:
        if licence["licence_number"] == licence_number:
            licence_found = True
            break

    if not licence_found:
        print("Driving licence not registered. Register it first.")
        return

    offences = load_data("offences.json")

    if len(offences) == 0:
        print("No offences available. Add an offence first.")
        return

    print("\nAvailable Offences:")

    for index, offence in enumerate(offences, start=1):
        print(index, ".", offence["name"], "- Rs.", offence["fine"])

    try:
        choice = int(input("Select offence number: "))

        if choice < 1 or choice > len(offences):
            print("Invalid offence selection.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    selected_offence = offences[choice - 1]
    offence_name = selected_offence["name"]
    fine = selected_offence["fine"]

    challans = load_data("challans.json")

    repeat_count = 0

    for challan in challans:
        if (challan["vehicle_number"] == vehicle_number
                and challan["offence"].lower() == offence_name.lower()):
            repeat_count += 1

    if repeat_count > 0:
        fine = fine * (repeat_count + 1)
        print("Repeat offence detected!")
        print("Increased fine: Rs.", fine)

    area = input("Enter offence area: ").strip()

    if area == "":
        print("Offence area cannot be empty.")
        return

    challan = {
        "challan_id": len(challans) + 1,
        "vehicle_number": vehicle_number,
        "licence_number": licence_number,
        "offence": offence_name,
        "offence_date": date.today().isoformat(),
        "area": area,
        "fine": fine,
        "status": "Pending"
    }

    challans.append(challan)
    save_data("challans.json", challans)

    print("\nChallan generated successfully!")
    print("Challan ID:", challan["challan_id"])
    print("Vehicle Number:", vehicle_number)
    print("Licence Number:", licence_number)
    print("Offence:", offence_name)
    print("Area:", area)
    print("Fine: Rs.", fine)
    print("Status: Pending")

    check_licence_status(licence_number)
