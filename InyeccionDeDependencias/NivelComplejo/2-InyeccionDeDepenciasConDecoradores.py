#Los decoradores permiten modificar dinámicamente el comportamiento de una función o clase. Aquí usamos un decorador para inyectar dependencias de manera automática.

# Decorador para inyección automática
def inyectar_servicios(func):
    def wrapper(*args, **kwargs):
        # Inyectamos una dependencia automáticamente
        kwargs['servicio'] = ServicioSaludo()
        return func(*args, **kwargs)
    return wrapper

# Servicio a inyectar
class ServicioSaludo:
    def saludar(self):
        return "¡Hola desde el decorador!"

# Clase que usa el decorador para inyectar
class Cliente:
    @inyectar_servicios
    def ejecutar(self, servicio=None):
        return servicio.saludar()

# Ejecutamos la clase sin pasar el servicio manualmente
cliente = Cliente()
print(cliente.ejecutar())  # Salida: ¡Hola desde el decorador!
