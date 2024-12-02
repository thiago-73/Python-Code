"""
Task Manager Program

This program allows the user to manage a list of tasks. The user can:
1. Add new tasks.
2. View the list of tasks.
3. Mark tasks as completed.
4. Remove completed tasks from the list.

Features:
- Handles invalid inputs gracefully.
- Uses a simple list to store tasks for easy manipulation.
- Provides clear options for managing tasks.

Example Interaction:
Task Manager Menu:
1. View tasks
2. Add a task
3. Mark a task as completed
4. Remove completed tasks
5. Exit
Enter your choice (1-5): 2
Enter the task title: Study for exams
Task 'Study for exams' added successfully.

Task Manager Menu:
1. View tasks
2. Add a task
3. Mark a task as completed
4. Remove completed tasks
5. Exit
Enter your choice (1-5): 1

Current Tasks:
1. Study for exams - Pending

Task Manager Menu:
1. View tasks
2. Add a task
3. Mark a task as completed
4. Remove completed tasks
5. Exit
Enter your choice (1-5): 3
Enter the task number to mark as completed: 1
Task 'Study for exams' marked as completed.

Task Manager Menu:
1. View tasks
2. Add a task
3. Mark a task as completed
4. Remove completed tasks
5. Exit
Enter your choice (1-5): 4
Completed tasks removed successfully.
"""
def show_tasks(tasks):
    """
    Displays the list of tasks along with their completion status.
    :param tasks: List of dictionaries representing tasks.
    """
    if not tasks:
        print("No tasks available.")
    else:
        print("\nCurrent Tasks:")
        for i, task in enumerate(tasks):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{i + 1}. {task['title']} - {status}")
    print()  # Blank line for better readability

def add_task(tasks):
    """
    Prompts the user to add a new task to the list.
    :param tasks: List of dictionaries representing tasks.
    """
    title = input("Enter the task title: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        print(f"Task '{title}' added successfully.\n")
    else:
        print("Task title cannot be empty.\n")

def mark_task_completed(tasks):
    """
    Allows the user to mark a task as completed.
    :param tasks: List of dictionaries representing tasks.
    """
    show_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]['completed'] = True
            print(f"Task '{tasks[task_num]['title']}' marked as completed.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def remove_completed_tasks(tasks):
    """
    Removes all completed tasks from the list.
    :param tasks: List of dictionaries representing tasks.
    """
    completed_tasks = [task for task in tasks if task['completed']]
    tasks[:] = [task for task in tasks if not task['completed']]
    if completed_tasks:
        print("Completed tasks removed successfully.\n")
    else:
        print("No completed tasks to remove.\n")

def main():
    """
    Main function for the Task Manager. Displays a menu and processes user input.
    """
    tasks = []  # List to store tasks
    while True:
        print("Task Manager Menu:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Mark a task as completed")
        print("4. Remove completed tasks")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 1:
                show_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                mark_task_completed(tasks)
            elif choice == 4:
                remove_completed_tasks(tasks)
            elif choice == 5:
                print("Exiting Task Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 5.\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")

# This ensures the script runs only when executed directly, not when imported as a module.
if __name__ == "__main__":
    main()
