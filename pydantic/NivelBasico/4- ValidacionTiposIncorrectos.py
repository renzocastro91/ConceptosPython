# Si se intenta pasar un valor de tipo incorrecto que no se pueda convertir, como en este caso ("cien" para el precio),
# Pydantic lanzará un error de validación indicando que el valor no es convertible a float.

# Modelos con validación de tipos incorrectos
from pydantic import BaseModel


class Producto(BaseModel):
    nombre: str
    precio: float


# Intentar pasar un valor incorrecto para precio
try:
    producto = Producto(nombre="Smartphone", precio="cien")
except Exception as e:
    print(e)  # Muestra un mensaje de error detallado
