#  Este ejemplo muestra cómo serializar un modelo de Pydantic a un diccionario o JSON. También se ilustra cómo deserializar
#  (convertir un diccionario de nuevo a un modelo). Esto es útil para trabajar con APIs o bases de datos donde los datos se
#  transfieren en estos formatos.

# Serialización y deserialización avanzada con `.dict()` y `.json()`
from pydantic import BaseModel

class Producto(BaseModel):
    nombre: str
    precio: float

# Crear un producto
producto = Producto(nombre="Auriculares", precio=100.50)

# Serialización a diccionario
producto_dict = producto.dict()  # Convierte a diccionario Python
print("Como diccionario:", producto_dict)

# Serialización a JSON
producto_json = producto.json()  # Convierte a formato JSON
print("Como JSON:", producto_json)

# Deserialización (crear un modelo a partir de un diccionario)
producto_desde_dict = Producto(**producto_dict)
print("Desde diccionario:", producto_desde_dict)


