# Aquí usamos el tipo Optional para definir que el campo descripcion es opcional. Si no se proporciona, su valor por
# defecto será None. Esto es útil cuando algunos campos no son obligatorios.

# Uso de campos opcionales (Optional)
from typing import Optional
from pydantic import BaseModel


class Producto(BaseModel):
    nombre: str
    descripcion: Optional[str] = None  # Este campo es opcional
    precio: float


# Crear un producto sin descripción
producto_sin_descripcion = Producto(nombre="Tablet", precio=250.00)
print(producto_sin_descripcion)

# Crear un producto con descripción
producto_con_descripcion = Producto(nombre="Laptop", descripcion="Laptop de 15 pulgadas", precio=999.99)
print(producto_con_descripcion)
