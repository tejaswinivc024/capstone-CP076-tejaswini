
from modules.storage import load_data


def view_all_challans():
    challans = load_data("challans.json")

    if len(challans) == 0:
        print("No challans available.")
        return

    print("\n========== ALL CHALLANS ==========")

    for challan in challans:
        print("Challan ID:", challan["challan_id"])
        print("Vehicle Number:", challan["vehicle_number"])
        print("Offence:", challan["offence"])
        print("Fine: Rs.", challan["fine"])
        print("Status:", challan["status"])
        print("----------------------------------")


def view_pending_challans():
    challans = load_data("challans.json")

    pending_challans = []

    for challan in challans:
        if challan["status"] == "Pending":
            pending_challans.append(challan)

    if len(pending_challans) == 0:
        print("No pending challans available.")
        return

    print("\n========== PENDING CHALLANS ==========")

    for challan in pending_challans:
        print("Challan ID:", challan["challan_id"])
        print("Vehicle Number:", challan["vehicle_number"])
        print("Offence:", challan["offence"])
        print("Fine: Rs.", challan["fine"])
        print("--------------------------------------")


def view_vehicle_dues():
    challans = load_data("challans.json")

    vehicle_number = input("Enter vehicle number: ").strip().upper()

    total_due = 0
    found = False

    print("\n========== VEHICLE PENDING DUES ==========")

    for challan in challans:
        if (challan["vehicle_number"] == vehicle_number
                and challan["status"] == "Pending"):

            found = True
            total_due += challan["fine"]

            print("Challan ID:", challan["challan_id"])
            print("Offence:", challan["offence"])
            print("Fine: Rs.", challan["fine"])
            print("------------------------------------------")

    if found:
        print("Total Amount Due: Rs.", total_due)
    else:
        print("No pending challans found for this vehicle.")
