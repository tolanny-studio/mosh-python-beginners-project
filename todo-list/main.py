from termcolor import colored, cprint

tasks = []


def view_task():
    if len(tasks) == 0:
        cprint("No task available 📪", "light_red")
        return
    for task_id, task in enumerate(tasks, start=1):
        cprint(f"{task_id}. {task}", "light_yellow")


def add_task():
    task_name = input("Enter task: ").capitalize()
    print()
    tasks.append(task_name)
    cprint(f'"{task_name}" added as task', "light_blue")


def remove_task():
    task_id = int(input("Enter task number: "))
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
    choice = int(input("Enter your choice 💽: "))
    print()
    return choice


def get_operation(operation_index):
    return operations[operation_index][1]


while True:
    display_operations()
    operation_choice = choose_operation()
    operation = get_operation(operation_choice)
    operation()
