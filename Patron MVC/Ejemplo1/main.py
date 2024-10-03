from controller import TaskController
from model import TaskModel
from view import TaskView


def main():
    model = TaskModel()
    view = TaskView()
    controller = TaskController(model, view)

    while True:
        print("\n1. Añadir tarea")
        print("2. Mostrar todas las tareas")
        print("3. Actualizar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        choice = input("Elige una opción: ")

        if choice == "1":
            controller.add_task()
        elif choice == "2":
            controller.display_all_tasks()
        elif choice == "3":
            controller.update_task()
        elif choice == "4":
            controller.remove_task()
        elif choice == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
