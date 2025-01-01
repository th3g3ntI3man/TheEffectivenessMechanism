# Employee Effectiveness Mechanism

The **Employee Effectiveness Mechanism** is a Python script designed to help you calculate the effectiveness of employees in your company based on their skills and match them to the most suitable roles.

## Features
- Calculates employee effectiveness using a custom formula based on required and actual stats.
- Assigns employees to roles such as:
  - Store Manager
  - Sexpert
  - Sales Assistant
- Replaces less efficient employees with better candidates from a pool of new employees.
- Identifies and lists new employees who are not efficient enough for the company.

## How It Works
### Employee Effectiveness Formula
The script uses the following formula to calculate employee efficiency:

\[
\text{efficiency} = \text{floor}(\min(45, \frac{\text{stat}}{\text{required}} \times 45)) + \text{floor}(\max(0, 5 \times \log_2(\frac{\text{stat}}{\text{required}})))
\]

This calculation is performed for both primary and secondary stats for each role.

### Role Definitions
Each role has specific requirements for primary and secondary stats:
- **Store Manager**:
  - Primary Stat: Endurance (8,000 required)
  - Secondary Stat: Intelligence (4,000 required)
- **Sexpert**:
  - Primary Stat: Intelligence (10,000 required)
  - Secondary Stat: Endurance (5,000 required)
- **Sales Assistant**:
  - Primary Stat: Endurance (4,000 required)
  - Secondary Stat: Manual Labor (2,000 required)

### Input Data
The script reads employee data from a `Stats.txt` file in the following format:

```
Current Employees:
Player1 1234 5678 9101
Player2 2345 6789 1011

New Employees:
Player3 3456 7890 1213
Player4 4567 8901 1314
```
- Each line represents an employee with their stats in the order: **Manual Labor, Intelligence, Endurance**.

## Setup
1. Place the script and the `Stats.txt` file in the same directory.
2. Run the script using Python.

## Usage
### Running the Script
Execute the script using:
```bash
python employee_effectiveness.py
```

### Interacting with the Script
- The script will prompt:
  ```
  Do you want to start the effectiveness mechanism? (y/n)
  ```
  - Enter `y` to process the employee effectiveness.
  - Enter `n` to exit the script.

### Output
The script displays:
- Total company effectiveness.
- Assigned roles and their effectiveness values.
- Employees replaced by new hires.
- New employees deemed inefficient.

### Example Output
```
Total Company Effectiveness -> 345⚡︎

Store Manager:
Player1 -> Store Manager 45⚡︎

Sexpert:
Player2 -> Sexpert 38⚡︎
Player3 -> Sexpert 35⚡︎

Sales Assistant:
Player4 -> Sales Assistant 30⚡︎
Player5 -> Sales Assistant 28⚡︎

Employees Replaced:
Player6 -> Replaced FIRE

New Employees Not Efficient for the Company:
Player7 is not efficient for the company.

The Employee Effectiveness Mechanism (Adult Novelties) by Jacket [3407347].
Any donations would be appreciated and your name will be added to the thread's credits.
```

## License
This script is distributed under the [MIT License](LICENSE).

## Contributing
Feel free to fork this repository and submit pull requests for improvements or new features.

## Acknowledgments
Created by **Jacket [3407347]**.

