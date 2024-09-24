# Este ejemplo muestra cómo manejar modelos anidados complejos y realizar validaciones a nivel de modelo padre.
# Aquí, Pedido contiene una lista de DetallePedido y validamos que al menos exista un producto en el pedido.

from typing import List
from pydantic import BaseModel, ValidationError, root_validator


# Definimos un modelo para el detalle de un pedido
class DetallePedido(BaseModel):
    producto: str
    cantidad: int


# Usamos el modelo DetallePedido dentro del modelo Pedido
class Pedido(BaseModel):
    id: int
    items: List[DetallePedido]

    # Validación compleja: asegurarse de que la cantidad total de productos sea al menos 1
    def total_items(self) -> int:
        return sum(item.cantidad for item in self.items)

    @root_validator
    def validar_total_items(cls, values):
        total = sum(item.cantidad for item in values.get('items', []))
        if total < 1:
            raise ValueError('El pedido debe contener al menos un producto')
        return values


# Pedido válido con productos
pedido_valido = Pedido(id=1, items=[DetallePedido(producto="Laptop", cantidad=1),
                                    DetallePedido(producto="Mouse", cantidad=2)])
print(pedido_valido)

# Intentar crear un pedido sin productos (esto lanzará un error)
try:
    pedido_invalido = Pedido(id=2, items=[])
except ValidationError as e:
    print(e)
