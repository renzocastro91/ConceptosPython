#  Pydantic permite generar automáticamente la documentación en formato JSON Schema, lo cual es extremadamente útil cuando se trabaja
#  con APIs que requieren especificaciones de contratos. Aquí, usamos .schema() para obtener el esquema de un modelo y otro que hereda
#  del primero.

from pydantic import BaseModel


class Usuario(BaseModel):
    id: int
    nombre: str
    email: str


# Modelo con más campos
class Admin(Usuario):
    permisos: str


# Generar el esquema JSON del modelo Usuario
esquema_usuario = Usuario.schema()
print("Esquema Usuario:", esquema_usuario)

# Generar el esquema JSON del modelo Admin
esquema_admin = Admin.schema()
print("Esquema Admin:", esquema_admin)
