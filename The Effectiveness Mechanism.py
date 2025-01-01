import math
import itertools
import os
import sys

def calculate_efficiency(primary_stat, primary_required, secondary_stat, secondary_required):
    try:
        primary_efficiency_base = math.floor(min(45, (primary_stat / primary_required) * 45))
        secondary_efficiency_base = math.floor(min(45, (secondary_stat / secondary_required) * 45))

        primary_bonus = math.floor(max(0, 5 * math.log2(primary_stat / primary_required))) if primary_stat > primary_required else 0
        secondary_bonus = math.floor(max(0, 5 * math.log2(secondary_stat / secondary_required))) if secondary_stat > secondary_required else 0

        total_efficiency = primary_efficiency_base + secondary_efficiency_base + primary_bonus + secondary_bonus
    except ValueError:
        total_efficiency = 0  # Handle invalid log inputs
    return total_efficiency

def get_stats_file_path():
    # Adjusted to find Stats.txt in the same directory as the script
    return os.path.join(os.path.dirname(__file__), "Stats.txt")

def read_player_data(filename):
    current_employees = []
    new_employees = []
    with open(filename, "r") as file:
        lines = file.readlines()
        current_section = None
        for line in lines:
            line = line.strip()
            if line == "Current Employees:":
                current_section = current_employees
            elif line == "New Employees:":
                current_section = new_employees
            elif line and current_section is not None:
                parts = line.split()
                username = parts[0]
                stats = list(map(int, parts[1:]))
                current_section.append((username, stats))
    return current_employees, new_employees

def calculate_efficiency_for_all_jobs(player, jobs):
    efficiencies = {}
    stats = player[1]  # [Manual Labor, Intelligence, Endurance]
    for job_name, requirements in jobs.items():
        primary_stat = stats[requirements["main_index"]]
        secondary_stat = stats[requirements["secondary_index"]]
        efficiency = calculate_efficiency(primary_stat, requirements["main_required"], secondary_stat, requirements["secondary_required"])
        efficiencies[job_name] = efficiency
    return efficiencies

def assign_jobs(current_employees, new_employees, jobs):
    all_employees = current_employees + new_employees
    assignments = {role: [] for role in jobs.keys()}
    total_efficiency = 0
    replaced_employees = []
    not_efficient_employees = []

    roles = [
        ("Store Manager", 1),
        ("Sexpert", 3),
        ("Sales Assistant", 5)
    ]

    for role, count in roles:
        role_requirements = jobs[role]
        role_candidates = []

        for employee in all_employees:
            efficiency = calculate_efficiency(
                employee[1][role_requirements["main_index"]],
                role_requirements["main_required"],
                employee[1][role_requirements["secondary_index"]],
                role_requirements["secondary_required"]
            )
            role_candidates.append((efficiency, employee))

        # Sort by efficiency descending and pick the top candidates for the role
        role_candidates.sort(reverse=True, key=lambda x: x[0])
        selected = role_candidates[:count]

        for efficiency, employee in selected:
            assignments[role].append((employee[0], efficiency))
            total_efficiency += efficiency

            # Remove assigned employee from the pool
            if employee in current_employees:
                current_employees.remove(employee)

            all_employees.remove(employee)

        # Fill remaining positions with placeholders if needed
        while len(assignments[role]) < count:
            assignments[role].append(("N/A", 0))

    # Any remaining current employees are considered replaced
    replaced_employees = [employee[0] for employee in current_employees]

    # Identify new employees not improving efficiency
    for _, employee in role_candidates[count:]:
        if employee in new_employees:
            not_efficient_employees.append(employee[0])

    return assignments, total_efficiency, replaced_employees, not_efficient_employees

def display_assignment(assignments, total_efficiency, replaced_employees, not_efficient_employees):
    sys.stdout.write("\033c")  # Clear the console
    print(f"Total Company Effectiveness -> {total_efficiency}⚡︎\n")

    for role, assigned_employees in assignments.items():
        print(f"{role}:")
        for player, effectiveness in assigned_employees:
            print(f"{player} -> {role} {effectiveness}⚡︎")
        print()

    if replaced_employees:
        print("\nEmployees Replaced:")
        for replaced_employee in replaced_employees:
            print(f"{replaced_employee} -> Replaced [31mFIRE[0m")

    if not_efficient_employees:
        print("\nNew Employees Not Efficient for the Company:")
        for player in not_efficient_employees:
            print(f"[31m{player}[0m is not efficient for the company.")

    print("\nThe Employee Effectiveness Mechanism (Adult Novelties) by Jacket [3407347].")
    print("Any donations would be appreciated and your name will be added to the thread's credits.")

def main():
    stats_file = get_stats_file_path()
    if not os.path.exists(stats_file):
        print(f"Error: {stats_file} does not exist.")
        return

    current_employees, new_employees = read_player_data(stats_file)

    jobs = {
        "Store Manager": {"main_required": 8000, "secondary_required": 4000, "main_index": 2, "secondary_index": 1},
        "Sexpert": {"main_required": 10000, "secondary_required": 5000, "main_index": 1, "secondary_index": 2},
        "Sales Assistant": {"main_required": 4000, "secondary_required": 2000, "main_index": 2, "secondary_index": 0}
    }

    while True:
        print("\nDo you want to start the effectiveness mechanism? (y/n)")
        choice = input().strip().lower()

        if choice == 'y':
            assignments, total_efficiency, replaced_employees, not_efficient_employees = assign_jobs(current_employees, new_employees, jobs)
            display_assignment(assignments, total_efficiency, replaced_employees, not_efficient_employees)
        elif choice == 'n':
            print("Exiting...")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
