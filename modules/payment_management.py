
from modules.storage import load_data, save_data


def record_payment():
    challans = load_data("challans.json")

    if len(challans) == 0:
        print("No challans available.")
        return

    try:
        challan_id = int(input("Enter challan ID: "))
    except ValueError:
        print("Please enter a valid challan ID.")
        return

    for challan in challans:
        if challan["challan_id"] == challan_id:

            if challan["status"] == "Paid":
                print("This challan has already been paid.")
                return

            print("\nChallan Details")
            print("Vehicle Number:", challan["vehicle_number"])
            print("Offence:", challan["offence"])
            print("Fine: Rs.", challan["fine"])

            confirm = input("Confirm payment? (yes/no): ").strip().lower()

            if confirm == "yes":
                challan["status"] = "Paid"
                save_data("challans.json", challans)
                print("Payment recorded successfully!")
            else:
                print("Payment cancelled.")

            return

    print("Challan ID not found.")
