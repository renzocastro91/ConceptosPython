# Este ejemplo introduce el uso de constr, un tipo restringido que permite definir condiciones como la longitud mínima y
# máxima de una cadena. Si los valores no cumplen con las restricciones, se lanza un error.

# Usando tipos avanzados con `constr`
from pydantic import BaseModel, constr


class Usuario(BaseModel):
    username: constr(min_length=3, max_length=12)  # Longitud mínima y máxima del nombre de usuario
    email: str


# Crear un usuario con un username válido
usuario = Usuario(username="user123", email="user123@example.com")
print(usuario)

# Intentar crear un usuario con un username inválido (menor de 3 caracteres)
try:
    usuario_invalido = Usuario(username="ab", email="ab@example.com")
except Exception as e:
    print(e)
