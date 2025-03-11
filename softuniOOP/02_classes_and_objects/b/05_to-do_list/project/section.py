from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for x in self.tasks:
            if x.name == task_name:
                x.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed = 0
        for y in self.tasks:
            if y.completed:
                self.tasks.remove(y)
                removed += 1
        return f"Cleared {removed} tasks."

    def view_section(self):
        to_return = f"Section {self.name}:"
        for z in self.tasks:
            to_return += f"\n{z.details()}"
        return to_return
