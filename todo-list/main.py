# To do list menu:
# 1. View Tasks
# 2. Add a task
# 3. Remove a task
# 4. Exit
# Enter your choice(1-4)

tasks = []


def view_task():
    print(tasks)


def add_task():
    print("Add task")
    task_id = int(input("Enter task number: "))
    task_name = input("Enter task ")
    tasks.append({task_id:task_name})


def remove_task():
    print("remove task")
    task_id = int(input("Enter task number: "))
    tasks.pop(task_id)
    


def exit_task():
    print("Exit task")
    exit()


operations = {
    1: ("View tasks", view_task),
    2: ("Add a task", add_task),
    3: ("Remove a task", remove_task),
    4: ("Exit", exit_task),
}


def display_operations():
    for operation_index, (operation_name, _) in operations.items():
        print(f"{operation_index}. {operation_name}")


def choose_operation():
    choice = int(input("Enter your choice: "))
    return choice


def get_operation(operation_index):
    return operations[operation_index][1]

while True:
    display_operations()
    operation_choice = choose_operation()
    operation = get_operation(operation_choice)
    operation()
