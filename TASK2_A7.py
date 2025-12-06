def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append(task)
    print(f" Task '{task}' added successfully!\n")

def view_tasks(tasks):
    if len(tasks) == 0:
        print(" No tasks found. Your to-do list is empty.\n")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks):
            print(f" {index + 1}. {task}")
        print()

def delete_task(tasks):
    if len(tasks) == 0:
        print(" No tasks to delete.\n")
        return

    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f" Task '{removed_task}' deleted successfully!\n")
        else:
            print(" Invalid task number. Please try again.\n")
    except ValueError:
        print(" Please enter a valid number.\n")
def main():
    tasks = []
    while True:
        print("========== TO-DO LIST MENU ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        print("====================================")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print(" Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print(" Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main()
