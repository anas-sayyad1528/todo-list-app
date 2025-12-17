import json
import os

# File to store tasks
FILE_NAME = "tasks.json"

# Global task list
tasks = []

def load_tasks():
    """Load tasks from file if it exists"""
    global tasks
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            tasks = json.load(file)

def save_tasks():
    """Save tasks to file"""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)

def display_tasks():
    """Display all tasks with their completion status"""
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i}. {task['task']} ({status})")

def add_task(task_name):
    """Add a new task"""
    if not task_name.strip():
        print("Task name cannot be empty.")
        return
    tasks.append({"task": task_name, "completed": False})
    save_tasks()
    print(f"Task '{task_name}' added successfully.")

def mark_completed(task_number):
    """Mark a task as completed"""
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks()
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def remove_task(task_number):
    """Remove a task after confirmation"""
    if 1 <= task_number <= len(tasks):
        confirm = input("Are you sure you want to delete this task? (y/n): ").lower()
        if confirm == 'y':
            removed_task = tasks.pop(task_number - 1)
            save_tasks()
            print(f"Task '{removed_task['task']}' removed.")
        else:
            print("Deletion cancelled.")
    else:
        print("Invalid task number.")

# Load tasks when program starts
load_tasks()

# Main loop
while True:
    print("\n-------------------------")
    print("1. Display to-do list")
    print("2. Add a task")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Quit")
    print("-------------------------")

    choice = input("Enter your choice: ")

    if choice == '1':
        display_tasks()

    elif choice == '2':
        task_name = input("Enter the task: ")
        add_task(task_name)

    elif choice == '3':
        display_tasks()
        try:
            task_number = int(input("Enter task number to mark as completed: "))
            mark_completed(task_number)
        except ValueError:
            print("Please enter a valid number.")

    elif choice == '4':
        display_tasks()
        try:
            task_number = int(input("Enter task number to remove: "))
            remove_task(task_number)
        except ValueError:
            print("Please enter a valid number.")

    elif choice == '5':
        print("\nThank you for using the To-Do List Application!")
        break

    else:
        print("Invalid choice. Please select between 1 and 5.")
