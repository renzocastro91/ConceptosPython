# Aquí Pydantic realiza una conversión automática. A pesar de que el precio se pasó como una cadena ("799.99"),
# el modelo lo convierte a un tipo float.

# Validación de tipos con Pydantic
from pydantic import BaseModel

class Producto(BaseModel):
    nombre: str
    precio: float

# Pydantic convierte automáticamente una cadena en un número flotante
producto = Producto(nombre="Laptop", precio="799.99")

# Mostrar los datos ya convertidos
print(producto)
