class TaskView:
    @staticmethod
    def display_tasks(tasks):
        if not tasks:
            print("No hay tareas.")
        else:
            for task in tasks:
                print(task)

    @staticmethod
    def get_task_description():
        return input("Ingresa la descripción de la tarea: ")

    @staticmethod
    def get_task_id():
        return int(input("Ingresa el ID de la tarea: "))

    @staticmethod
    def task_added_successfully(task):
        print(f"Tarea '{task.description}' añadida con éxito.")

    @staticmethod
    def task_removed_successfully(task_id):
        print(f"Tarea con ID {task_id} eliminada con éxito.")
