#En entornos web, como el framework FastAPI, la inyección de dependencias se utiliza para gestionar servicios como bases de datos, autenticación, etc. Aquí mostramos un ejemplo básico de cómo usar inyección de dependencias en FastAPI.

from fastapi import FastAPI, Depends

# Servicio de saludo
class ServicioSaludo:
    def saludar(self):
        return "¡Hola desde FastAPI!"

# Función para inyectar la dependencia
def obtener_servicio_saludo():
    return ServicioSaludo()

# Crear la app FastAPI
app = FastAPI()

# Definir la ruta que utiliza inyección de dependencias
@app.get("/saludo")
def saludo(servicio_saludo: ServicioSaludo = Depends(obtener_servicio_saludo)):
    return {"mensaje": servicio_saludo.saludar()}


# Si ejecutas la app con uvicorn, por ejemplo con: uvicorn nombre_del_archivo:app --reload
# Podrás acceder a la ruta /saludo y ver el resultado:
# {"mensaje": "Hola desde FastAPI!"}
