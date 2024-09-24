# Este ejemplo introduce validaciones personalizadas utilizando el decorador @validator. La función verificar_edad
# asegura que la edad sea mayor o igual a 18, y si no lo es, se lanza una excepción.

# Uso de validaciones con `@validator`
from pydantic import BaseModel, validator


class Usuario(BaseModel):
    nombre: str
    edad: int

    # Validación personalizada: verificar que la edad sea mayor o igual a 18
    @validator('edad')
    def verificar_edad(cls, v):
        if v < 18:
            raise ValueError('La edad debe ser mayor o igual a 18')
        return v


# Probar con una edad válida
usuario = Usuario(nombre="Pedro", edad=20)
print(usuario)

# Probar con una edad inválida, esto lanzará un error
try:
    usuario_invalido = Usuario(nombre="Juan", edad=15)
except Exception as e:
    print(e)
