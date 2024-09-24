#  En este ejemplo se valida que la lista de productos no esté vacía. Si la lista no contiene al menos un producto,
#  se lanza un error. Esto es útil para asegurar que ciertos campos que son listas cumplan condiciones específicas.

# Validación de listas
from typing import List
from pydantic import BaseModel, validator


class Pedido(BaseModel):
    productos: List[str]  # Lista de productos

    # Validación personalizada: verificar que la lista tenga al menos un producto
    @validator('productos')
    def validar_productos(cls, v):
        if len(v) == 0:
            raise ValueError('Debe haber al menos un producto en el pedido')
        return v


# Crear un pedido válido
pedido_valido = Pedido(productos=["Laptop", "Mouse"])
print(pedido_valido)

# Intentar crear un pedido sin productos (esto lanzará un error)
try:
    pedido_invalido = Pedido(productos=[])
except Exception as e:
    print(e)
