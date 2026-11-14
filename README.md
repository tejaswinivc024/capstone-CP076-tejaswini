# ChallanTrack – Traffic Violation and Penalty Management System

## Project Overview

ChallanTrack is a Python-based Traffic Violation and Penalty Management System designed to simplify the process of recording traffic violations, issuing challans, managing fine payments, and tracking repeat offenders.

The system helps maintain organized records of traffic offences and provides an easy way to monitor pending challans and outstanding fines for vehicles.

## Problem Statement

Traffic police need an efficient way to issue fines quickly, maintain violation records, and identify vehicles with repeated traffic offences. Managing these records manually can make it difficult to track payments and repeat offenders.

ChallanTrack aims to address these challenges through a simple and organized digital system.

## Objectives

- Maintain a record of traffic offences and their fine amounts.
- Issue challans to vehicles after validating vehicle registration numbers.
- Identify repeat offences and increase fines accordingly.
- Record challan payment details.
- Display pending challans and total outstanding amounts for vehicles.

## Core Features

1. **Offence Management:** Maintain traffic offence names and their corresponding fine amounts.
2. **Challan Generation:** Issue challans to vehicles after checking vehicle number format.
3. **Repeat Offender Management:** Increase fines for repeated offences by the same vehicle.
4. **Payment Tracking:** Record payments made against challans.
5. **Pending Challan Management:** List unpaid challans by vehicle and calculate the total amount due.

## Optional Features

- Suspend a driving licence after a specified number of offences within a year.
- Generate reports showing the most common traffic offences by area.

## Technology Stack

- **Programming Language:** Python
- **Development Environment:** Visual Studio Code
- **Data Storage:** JSON
- **Version Control:** Git and GitHub

## Project Structure

```text
capstone-CP076-tejaswini/
│
├── main.py
├── data/
│   ├── offences.json
│   └── challans.json
│
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
4. Run the application:

   ```bash
   python main.py
   ```

## Expected Outcome

ChallanTrack will provide a simple and user-friendly system for managing traffic violations, generating challans, tracking payments, and identifying repeat offenders.

## Project Information

- **Project Code:** CP-076
- **Project Name:** ChallanTrack
- **Domain:** Public Services, Utilities and Smart City
- **Project Level:** Foundation
- **Programming Language:** Python