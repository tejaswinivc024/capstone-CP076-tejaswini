
from modules.storage import load_data


def generate_area_report():
    challans = load_data("challans.json")

    if len(challans) == 0:
        print("No challan records available.")
        return

    area_reports = {}

    for challan in challans:
        area = challan.get("area")
        offence = challan["offence"]

        if not area:
            continue

        if area not in area_reports:
            area_reports[area] = {}

        if offence not in area_reports[area]:
            area_reports[area][offence] = 0

        area_reports[area][offence] += 1

    if len(area_reports) == 0:
        print("No area-wise records available.")
        return

    print("\n========== AREA-WISE OFFENCE REPORT ==========")

    for area, offences in area_reports.items():
        print("\nArea:", area)

        for offence, count in offences.items():
            print(offence, ":", count, "cases")

        most_common = max(offences, key=offences.get)

        print("Most Common Offence:", most_common)
        print("Number of Cases:", offences[most_common])
        print("----------------------------------------------")
