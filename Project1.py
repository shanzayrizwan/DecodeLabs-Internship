class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        task = {
            "id": len(self.tasks) + 1,
            "task": task_name
        }
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for task in self.tasks:
                print(f"{task['id']}. {task['task']}")


def main():
    todo = TodoList()

    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo.add_task(task)

        elif choice == "2":
            todo.view_tasks()

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
