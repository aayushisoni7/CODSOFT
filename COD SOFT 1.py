class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print(f"Task '{task}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for idx, task in enumerate(self.tasks):
                status = "Done" if task['completed'] else "Not Done"
                print(f"{idx + 1}. {task['task']} - {status}")

    def update_task(self, task_index, new_task):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['task'] = new_task
            print(f"Task {task_index + 1} updated to '{new_task}'.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task['task']}' deleted.")
        else:
            print("Invalid task number.")

    def mark_task_complete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
            print(f"Task {task_index + 1} marked as complete.")
        else:
            print("Invalid task number.")

def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Complete")
    print("6. Exit")

def main():
    todo_list = ToDoList()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_index, new_task)
        elif choice == '4':
            task_index = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == '5':
            task_index = int(input("Enter the task number to mark as complete: ")) - 1
            todo_list.mark_task_complete(task_index)
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
