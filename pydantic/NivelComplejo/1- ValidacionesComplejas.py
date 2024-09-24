#  Este ejemplo usa @root_validator, que es útil cuando necesitas validar la consistencia entre múltiples campos (como contraseñas).
#  Aquí, validamos que password y confirm_password coincidan, y lanzamos un error si no lo hacen.

from pydantic import BaseModel, root_validator, ValidationError


class Usuario(BaseModel):
    nombre: str
    password: str
    confirm_password: str

    # Usamos root_validator para validar múltiples campos a la vez
    @root_validator
    def verificar_passwords(cls, values):
        password = values.get('password')
        confirm_password = values.get('confirm_password')
        if password != confirm_password:
            raise ValueError('Las contraseñas no coinciden')
        return values


# Crear un usuario con contraseñas coincidentes
usuario_valido = Usuario(nombre="Carlos", password="12345", confirm_password="12345")
print(usuario_valido)

# Intentar crear un usuario con contraseñas no coincidentes (esto lanzará un error)
try:
    usuario_invalido = Usuario(nombre="Carlos", password="12345", confirm_password="54321")
except ValidationError as e:
    print(e)
