"""Simple To-Do List Application

Allows users to manage tasks in a to-do list using the command line. To-do
list is read from and saved to a file. The program keeps a record of the
number of tasks completed and remaining."""

filename = "todolist.txt"
try:
    with open(filename, "r") as f:
        to_do_list = f.readlines()
        to_do_list = [task.strip() for task in to_do_list]
except FileNotFoundError:
    to_do_list = []

remaining_tasks = 0
completed_tasks = 0

def display_menu():
    """Displays the menu"""
    print("To-Do List Manager")
    print("______________________")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")

    choice = input("\nPlease enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        with open(filename, "w") as f:
            for task in to_do_list:
                f.write(task + "\n")

        print("Goodbye!")
        exit()
    else:
        print("Please enter a valid choice.")


def add_task():
    """Adds a new task to the to-do list"""
    global remaining_tasks
    new_task = input("Please enter a new task: ")
    to_do_list.append(new_task)
    remaining_tasks += 1
    print("Task added!")
    reset = input("Hit enter to return to the main menu.")
    if reset == "":
        display_menu()


def mark_complete():
    """Marks the task as complete"""
    global completed_tasks
    global remaining_tasks
    if len(to_do_list) > 0:
        for i, task in enumerate(to_do_list, start=1):
            print(f"{i}: {task}")
        del_task = input("\nPlease enter the numbr of the task to complete: ")
        to_do_list.pop(int(del_task)-1)
        completed_tasks += 1
        remaining_tasks -= 1
        print("Task marked complete!")
        print("Tasks Completed: ", completed_tasks)
        print("Tasks remaining: ", remaining_tasks)
    else:
        print("There are no tasks on the list...")
    reset = input("Hit enter to return to the main menu.")
    if reset == "":
        display_menu()


def view_tasks():
    """Views the to-do list"""
    if len(to_do_list) > 0:
        for i, task in enumerate(to_do_list, start=1):
            print(f"{i}: {task}")
    else:
        print("There are no tasks on the list...")
    reset = input("Hit enter to return to the main menu.")
    if reset == "":
        display_menu()


def delete_task():
    """Deletes the task without marking it complete"""
    global remaining_tasks
    if len(to_do_list) > 0:
        for i, task in enumerate(to_do_list, start=1):
            print(f"{i}: {task}")
        del_task = input("\nPlease enter the numbr of the task to delete: ")
        to_do_list.pop(int(del_task) - 1)
        remaining_tasks -= 1
        print("Task deleted!")
        print("Tasks remaining: ", remaining_tasks)
    else:
        print("There are no tasks on the list...")
    reset = input("Hit enter to return to the main menu.")
    if reset == "":
        display_menu()

display_menu()
