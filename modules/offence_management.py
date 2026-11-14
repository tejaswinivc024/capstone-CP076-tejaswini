
from modules.storage import load_data, save_data


def add_offence():
    offences = load_data("offences.json")

    name = input("Enter offence name: ").strip()

    if name == "":
        print("Offence name cannot be empty.")
        return

    for offence in offences:
        if offence["name"].lower() == name.lower():
            print("This offence already exists.")
            return

    try:
        fine = int(input("Enter fine amount: "))

        if fine <= 0:
            print("Fine amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    offence = {
        "name": name,
        "fine": fine
    }

    offences.append(offence)
    save_data("offences.json", offences)

    print("Offence added successfully!")


def view_offences():
    offences = load_data("offences.json")

    if len(offences) == 0:
        print("No offences available.")
        return

    print("\n------ TRAFFIC OFFENCES ------")

    for offence in offences:
        print("Offence:", offence["name"])
        print("Fine: Rs.", offence["fine"])
        print("------------------------------")
