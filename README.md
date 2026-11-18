CP-076 ChallanTrack: Traffic Violation and Penalty Management System

Team

- Tejaswini V C – 1AT24CS238
- Sony R – 1AT24CS213
- Track: Python

Project Overview

ChallanTrack is a Python-based Traffic Violation and Penalty Management System designed to simplify the process of managing traffic offences, generating challans, tracking payments and identifying repeat offenders.

The system allows users to maintain offence records, validate vehicle registration numbers, calculate increased fines for repeated violations and monitor pending challan payments. It also provides driving licence status management and area-wise offence reports.

The application uses JSON files to store and manage records.

How to Run

Prerequisites:

- Python 3.x installed on the system.
- Git (if cloning the repository).

Step 1: Clone the repository

git clone https://github.com/tejaswinivc024/capstone-CP076-tejaswini.git

Step 2: Navigate to the project directory

cd capstone-CP076-tejaswini

Step 3: Run the application

python challantrack.py

Features That Work

1. Offence Management
   
   - Add new traffic offences with their respective fine amounts.
   - View the list of available offences.
   - Prevent duplicate offence entries.

2. Vehicle Number Validation
   
   - Validate vehicle registration numbers using a predefined format.
   - Prevent challan generation for invalid vehicle numbers.

3. Challan Generation
   
   - Generate challans by selecting an offence and entering vehicle and driving licence details.
   - Store challan details, including offence date, area, fine amount and payment status.

4. Repeat Offender Management
   
   - Identify repeated offences committed by the same vehicle.
   - Automatically increase the fine amount for repeated violations of the same offence.

5. Payment Management
   
   - Record payments against generated challans.
   - Update challan status to Paid after successful payment confirmation.
   - Prevent duplicate payments for already-paid challans.

6. Pending Challan Management
   
   - View all generated challans.
   - Display pending challans.
   - Search pending dues using a vehicle number.
   - Calculate the total outstanding amount for a vehicle.

7. Driving Licence Management
   
   - Register driving licences.
   - Check the current licence status.
   - Track offences associated with a registered licence.

8. Driving Licence Suspension
   
   - Count offences committed within the last year.
   - Automatically suspend a licence when the offence count reaches 5 or more.

9. Area-wise Offence Report
   
   - Generate reports based on the areas where offences occurred.
   - Display offence counts for each area.
   - Identify the most common offence in each area.

Technologies Used

- Programming Language: Python
- Data Storage: JSON
- Development Environment: Visual Studio Code
- Version Control: Git
- Repository Hosting: GitHub

Project Structure

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

Sample Run

========================================
             CHALLANTRACK
 Traffic Violation and Penalty Management
========================================
1. Offence Management
2. Generate Challan
3. View All Challans
4. Record Challan Payment
5. View Pending Challans
6. View Vehicle Pending Dues
7. Driving Licence Management
8. Area-wise Offence Report
9. Exit
========================================
Enter your choice (1-9):

GitHub Repository

"ChallanTrack – CP-076" (https://github.com/tejaswinivc024/capstone-CP076-tejaswini.git)
