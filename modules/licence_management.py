
from datetime import date
from modules.storage import load_data, save_data


SUSPENSION_LIMIT = 5


def add_licence():
    licences = load_data("licences.json")

    licence_number = input("Enter driving licence number: ").strip().upper()

    if licence_number == "":
        print("Licence number cannot be empty.")
        return

    for licence in licences:
        if licence["licence_number"] == licence_number:
            print("This licence is already registered.")
            return

    licence = {
        "licence_number": licence_number,
        "status": "Active"
    }

    licences.append(licence)
    save_data("licences.json", licences)

    print("Driving licence registered successfully!")


def check_licence_status(licence_number):
    licences = load_data("licences.json")
    challans = load_data("challans.json")

    for licence in licences:
        if licence["licence_number"] == licence_number:

            offence_count = 0
            today = date.today()

            for challan in challans:
                if challan.get("licence_number") == licence_number:
                    offence_date = challan.get("offence_date")

                    if offence_date:
                        offence_date = date.fromisoformat(offence_date)
                        days = (today - offence_date).days

                        if 0 <= days <= 365:
                            offence_count += 1

            if offence_count >= SUSPENSION_LIMIT:
                licence["status"] = "Suspended"
            else:
                licence["status"] = "Active"

            save_data("licences.json", licences)

            print("Offences in the last year:", offence_count)
            print("Licence Status:", licence["status"])
            return

    print("Driving licence not found.")
