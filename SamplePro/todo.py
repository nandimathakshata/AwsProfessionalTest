# todo.py

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        return f"Task '{task}' added."

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return f"Task '{task}' removed."
        else:
            return f"Task '{task}' not found."

    def view_tasks(self):
        if not self.tasks:
            return "No tasks in the list."
        return "\n".join(f"{idx + 1}. {task}" for idx, task in enumerate(self.tasks))