class InventoryController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_product(self):
        name = self.view.get_product_name()
        quantity = self.view.get_product_quantity()
        product = self.model.add_product(name, quantity)
        self.view.product_added_successfully(product)

    def display_all_products(self):
        products = self.model.get_all_products()
        self.view.display_products(products)

    def update_product(self):
        product_id = self.view.get_product_id()
        new_quantity = self.view.get_product_quantity()
        self.model.update_product(product_id, new_quantity)
        print(f"Producto con ID {product_id} actualizado con éxito.")

    def remove_product(self):
        product_id = self.view.get_product_id()
        self.model.remove_product(product_id)
        self.view.product_removed_successfully(product_id)
