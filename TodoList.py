class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task added: {task}")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            print(f"Task removed: {self.tasks[index]}")
            self.tasks.pop(index)
        else:
            print("Invalid index")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

def main():
    my_list = ToDoList()
    while True:
        print("Choose an option:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Display tasks")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            my_list.add_task(task)
        elif choice == '2':
            try:
                index = int(input("Enter index of task to remove: ")) - 1
                my_list.remove_task(index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '3':
            my_list.display_tasks()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        print()

if __name__ == "__main__":
    main()
