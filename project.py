tasks = []
statuses = []


def display_menu():
    print("\n" + "=" * 32)
    print("      TO-DO LIST MANAGER")
    print("=" * 32)
    print("[1] Add Task")
    print("[2] View Tasks")
    print("[3] Mark Task as Completed")
    print("[4] Delete Task")
    print("[5] Show Summary")
    print("[6] Exit")


def add_task():
    task = input("Enter task: ")

    tasks.append(task)
    statuses.append("Pending")

    print("Task added successfully!")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
        return

    print("\nTASK LIST")
    print("-" * 40)

    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]} - {statuses[i]}")


def complete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    task_num = int(input("Enter task number to complete: "))

    if 1 <= task_num <= len(tasks):
        statuses[task_num - 1] = "Completed"
        print("Task marked as completed!")
    else:
        print("Invalid task number!")


def delete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    task_num = int(input("Enter task number to delete: "))

    if 1 <= task_num <= len(tasks):
        tasks.pop(task_num - 1)
        statuses.pop(task_num - 1)

        print("Task deleted successfully!")
    else:
        print("Invalid task number!")


def show_summary():
    total_tasks = len(tasks)
    completed = statuses.count("Completed")
    pending = statuses.count("Pending")

    print("\nSUMMARY")
    print("-" * 20)
    print(f"Total Tasks: {total_tasks}")
    print(f"Completed : {completed}")
    print(f"Pending   : {pending}")


def main():
    while True:
        display_menu()

        choice = input("Enter choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            show_summary()

        elif choice == "6":
            print("Thank you for using To-Do List Manager!")
            break

        else:
            print("Invalid choice!")


main()

