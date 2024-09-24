# Este es el ejemplo más básico de cómo crear un esquema con Pydantic usando el BaseModel.
#Se valida que los tipos de datos coincidan con los definidos en el modelo (str para nombre y int para edad).

# Definir un modelo básico de Pydantic
from pydantic import BaseModel

# Definimos un esquema con dos campos: nombre (str) y edad (int)
class Persona(BaseModel):
    nombre: str
    edad: int

# Crear una instancia del modelo
persona = Persona(nombre="Juan", edad=30)

# Mostrar los datos de la instancia
print(persona)
