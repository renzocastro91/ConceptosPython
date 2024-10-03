from controller import InventoryController
from model import InventoryModel
from view import InventoryView


def main():
    model = InventoryModel()
    view = InventoryView()
    controller = InventoryController(model, view)

    while True:
        print("\n1. Añadir producto")
        print("2. Mostrar inventario")
        print("3. Actualizar cantidad de producto")
        print("4. Eliminar producto")
        print("5. Salir")

        choice = input("Elige una opción: ")

        if choice == "1":
            controller.add_product()
        elif choice == "2":
            controller.display_all_products()
        elif choice == "3":
            controller.update_product()
        elif choice == "4":
            controller.remove_product()
        elif choice == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
