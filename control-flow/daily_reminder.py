task = input("Enter task description: ")
priority = input("task's priority (High, Medium, low): ").lower()
time_bound = input("Is the task time bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a high priority task. Consider completing it when you have free time")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a medium priority task. Consider completing it when you have free time")
    case "low":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Enter (high, medium or low)")