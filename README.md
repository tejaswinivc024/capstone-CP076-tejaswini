# ChallanTrack – Traffic Violation and Penalty Management System

## Project Overview

ChallanTrack is a Python-based Traffic Violation and Penalty Management System designed to simplify the process of recording traffic violations, issuing challans, managing fine payments, and tracking repeat offenders.

The system maintains organized records of traffic offences and provides an easy way to monitor pending challans, outstanding fines, driving licence status, and area-wise offence statistics.

## Problem Statement

Traffic police need an efficient way to issue fines, maintain violation records, and identify vehicles with repeated traffic offences. Managing these records manually can make it difficult to track payments, monitor driving licence status, and identify areas with frequent traffic violations.

ChallanTrack aims to address these challenges through a simple and organized digital system.

## Objectives

- Maintain a record of traffic offences and their fine amounts.
- Issue challans to vehicles after validating vehicle registration numbers.
- Identify repeat offences and increase fines accordingly.
- Record challan payments.
- Display pending challans and total outstanding amounts for vehicles.
- Monitor driving licence status based on offences committed within one year.
- Generate reports showing common traffic offences in different areas.

## Core Features

1. **Offence Management:** Add and view traffic offences with their corresponding fine amounts.
2. **Vehicle Number Validation:** Validate vehicle registration number formats before generating challans.
3. **Challan Generation:** Generate challans for vehicles based on selected traffic offences.
4. **Repeat Offender Management:** Increase fines for repeated offences by the same vehicle.
5. **Payment Tracking:** Record challan payments and update payment status.
6. **Pending Challan Management:** View unpaid challans and calculate the total pending amount for a vehicle.
7. **Driving Licence Management:** Register driving licences and check their current status.
8. **Driving Licence Suspension:** Automatically suspend a driving licence when the licence holder receives 5 or more offences within a year.
9. **Area-wise Offence Reports:** Generate reports showing the number of different traffic offences recorded in each area and identify the most common offence.

## Technology Stack

- **Programming Language:** Python
- **Development Environment:** Visual Studio Code
- **Data Storage:** JSON
- **Libraries:** Python Standard Library
- **Version Control:** Git and GitHub

## Project Structure

```text
capstone-CP076-tejaswini/
│
├── data/
│   ├── offences.json
│   ├── challans.json
│   └── licences.json
│
├── modules/
│   ├── __init__.py
│   ├── storage.py
│   ├── offence_management.py
│   ├── vehicle_validation.py
│   ├── challan_management.py
│   ├── payment_management.py
│   ├── reports.py
│   ├── licence_management.py
│   └── area_reports.py
│
├── challantrack.py
├── README.md
└── .gitignore
```

## How to Run

1. Install Python on your system.
2. Clone this repository:

   ```bash
   git clone https://github.com/tejaswinivc024/capstone-CP076-tejaswini.git
   ```

3. Open the project folder in Visual Studio Code.
4. Run the application from the project root directory:

   ```bash
   python challantrack.py
   ```

## Expected Outcome

ChallanTrack provides a simple menu-driven application for managing traffic violations, generating challans, tracking payments, identifying repeat offenders, monitoring driving licence status, and analysing area-wise traffic offence records.

The application uses JSON files to store offence details, challan records, and driving licence information.

## Project Information

- **Project Code:** CP-076
- **Project Name:** ChallanTrack
- **Domain:** Public Services, Utilities and Smart City
- **Project Level:** Foundation
- **Programming Language:** Python