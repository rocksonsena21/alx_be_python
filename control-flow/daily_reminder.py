
# Loop to ensure valid input from user
while True:
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").lower().strip()
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

    if priority in ["high", "medium", "low"] and time_bound in ["yes", "no"]:
        break
    else:
        print("\nInvalid input detected. Please try again.\n")


# Match Case for priority levels
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unspecified priority"


# Modify message based on time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
    print("\nReminder:", message)
else:
    message += ". Consider completing it when you have free time."
    print("\nNote:", message)
