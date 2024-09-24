# Los modelos de Pydantic permiten definir valores por defecto para los campos. En este ejemplo, si no se proporciona
# el valor para is_active, toma automáticamente el valor True.

# Valores por defecto en los modelos
from pydantic import BaseModel


class Usuario(BaseModel):
    username: str
    is_active: bool = True  # Valor por defecto


# Crear una instancia del modelo sin especificar el campo is_active
usuario = Usuario(username="admin")

# El campo is_active toma el valor por defecto True
print(usuario)
