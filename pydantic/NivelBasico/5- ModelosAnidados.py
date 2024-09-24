# Este ejemplo muestra cómo Pydantic permite anidar modelos. Aquí, el modelo Usuario tiene un campo direccion que es un
# modelo Direccion anidado, lo que permite trabajar con datos más complejos.

# Modelos anidados (un modelo dentro de otro)
from pydantic import BaseModel


# Definimos un modelo para la dirección
class Direccion(BaseModel):
    calle: str
    ciudad: str


# Usamos el modelo de Dirección dentro del modelo Usuario
class Usuario(BaseModel):
    nombre: str
    direccion: Direccion  # Campo anidado


# Crear una instancia del modelo Usuario con un modelo Dirección
usuario = Usuario(nombre="Carlos", direccion={"calle": "Calle Falsa 123", "ciudad": "Lima"})

# Mostrar la instancia de Usuario, incluyendo los datos de la dirección anidada
print(usuario)
