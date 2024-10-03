class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_task(self):
        description = self.view.get_task_description()
        task = self.model.add_task(description)
        self.view.task_added_successfully(task)

    def display_all_tasks(self):
        tasks = self.model.get_all_tasks()
        self.view.display_tasks(tasks)

    def update_task(self):
        task_id = self.view.get_task_id()
        new_description = self.view.get_task_description()
        self.model.update_task(task_id, new_description)
        print(f"Tarea con ID {task_id} actualizada con éxito.")

    def remove_task(self):
        task_id = self.view.get_task_id()
        self.model.remove_task(task_id)
        self.view.task_removed_successfully(task_id)
