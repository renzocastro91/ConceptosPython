# Aquí usamos un custom error handler con un metodo @classmethod para personalizar cómo se manejan los errores de
#  validación. El validador para username asegura que no contenga espacios.

from pydantic import BaseModel, validator, ValidationError


class Usuario(BaseModel):
    username: str
    edad: int

    # Validación avanzada de username
    @validator('username')
    def validar_username(cls, v):
        if ' ' in v:
            raise ValueError('El nombre de usuario no puede contener espacios')
        return v

    # Metodo personalizado para manejar errores de forma detallada
    @classmethod
    def crear_usuario(cls, **kwargs):
        try:
            return cls(**kwargs)
        except ValidationError as e:
            # Aquí personalizamos el mensaje de error
            print(f"Error al crear usuario: {e}")
            raise


# Crear un usuario con un username válido
usuario = Usuario.crear_usuario(username="usuario123", edad=25)
print(usuario)

# Intentar crear un usuario con espacios en el username (esto lanzará un error)
try:
    usuario_invalido = Usuario.crear_usuario(username="usuario 123", edad=25)
except ValidationError as e:
    pass
