class InventoryView:
    @staticmethod
    def display_products(products):
        if not products:
            print("El inventario está vacío.")
        else:
            for product in products:
                print(product)

    @staticmethod
    def get_product_name():
        return input("Ingresa el nombre del producto: ")

    @staticmethod
    def get_product_quantity():
        return int(input("Ingresa la cantidad del producto: "))

    @staticmethod
    def get_product_id():
        return int(input("Ingresa el ID del producto: "))

    @staticmethod
    def product_added_successfully(product):
        print(f"Producto '{product.name}' añadido con éxito.")

    @staticmethod
    def product_removed_successfully(product_id):
        print(f"Producto con ID {product_id} eliminado con éxito.")
