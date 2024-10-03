class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id
        self.description = description
        self.completed = False

    def complete_task(self):
        self.completed = True

    def __str__(self):
        status = "Completada" if self.completed else "Pendiente"
        return f"Tarea {self.task_id}: {self.description} [{status}]"


class TaskModel:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, description):
        task = Task(self.next_id, description)
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task

    def get_all_tasks(self):
        return list(self.tasks.values())

    def update_task(self, task_id, description):
        if task_id in self.tasks:
            self.tasks[task_id].description = description

    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
