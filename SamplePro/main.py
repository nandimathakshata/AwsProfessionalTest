# main.py

from todo import ToDoList

def display_menu():
    print("To-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

def main():
    todo_list = ToDoList()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            print(todo_list.add_task(task))
        elif choice == '2':
            task = input("Enter the task to remove: ")
            print(todo_list.remove_task(task))
        elif choice == '3':
            print("Tasks:")
            print(todo_list.view_tasks())
        elif choice == '5':
            print("Exiting the application...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()