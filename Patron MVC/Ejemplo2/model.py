class Product:
    def __init__(self, product_id, name, quantity):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity

    def update_quantity(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return (
            f"ID: {self.product_id} | Producto: {self.name} | "
            f"Cantidad: {self.quantity}"
        )


class InventoryModel:
    def __init__(self):
        self.products = {}
        self.next_id = 1

    def add_product(self, name, quantity):
        product = Product(self.next_id, name, quantity)
        self.products[self.next_id] = product
        self.next_id += 1
        return product

    def get_all_products(self):
        return list(self.products.values())

    def update_product(self, product_id, quantity):
        if product_id in self.products:
            self.products[product_id].update_quantity(quantity)

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
