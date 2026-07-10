from sys import exit
from termcolor import cprint

tasks = []


def view_task():
    if not tasks:
        cprint("No task available 📪", "light_red")
        return
    for task_id, task in enumerate(tasks, start=1):
        cprint(f"{task_id}. {task}", "light_yellow")


def validate_task_input(prompt):
    task = input(prompt).strip().title()
    if len(task) < 3:
        cprint("Invalid task ⛔", "light_red")
        return None
    if task in tasks:
        cprint("Task is present in task list ⛔", "light_red")
        return None
    return task


def add_task():
    task_name = validate_task_input("Enter task: ")
    if task_name:
        print()
        tasks.append(task_name)
        cprint(f'"{task_name}" added as task', "light_blue")


def validate_remove_task(task_index):
    try:
        task_number = int(input(task_index))
    except ValueError:
        cprint("Invalid task ⛔", "light_red")
        return None

    if task_number == 0 or task_number > len(tasks):
        cprint("Invalid task number⛔", "light_red")
        return None
    return task_number


def remove_task():
    if not tasks:
        cprint("No task available 📪", "light_red")
        return
    task_id = validate_remove_task("Enter task number: ")
    if task_id:
        removed_task = tasks.pop(task_id - 1)
        print()
        cprint(f"{removed_task} removed", "light_red")
        print()
        print("Current task")
        print()
        view_task()


def exit_task():
    cprint("Exit todo", "cyan")
    print()
    exit()


operations = {
    1: ("View tasks", view_task),
    2: ("Add a task", add_task),
    3: ("Remove a task", remove_task),
    4: ("Exit", exit_task),
}


def display_operations():
    print()
    for operation_index, (operation_name, _) in operations.items():
        cprint(f"{operation_index}. {operation_name}", "dark_grey")
    print()


def choose_operation():
    try:
        choice = int(input("Enter your choice 💽: "))
    except ValueError:
        cprint("Invalid operation ⛔", "light_red")
        return None
    if choice not in operations:
        cprint("Invalid operation index ⛔", "light_red")
        return None
    print()
    return choice


def get_operation(operation_index):
    return operations[operation_index][1]


while True:
    display_operations()
    operation_choice = choose_operation()
    if operation_choice:
        get_operation(operation_choice)()
