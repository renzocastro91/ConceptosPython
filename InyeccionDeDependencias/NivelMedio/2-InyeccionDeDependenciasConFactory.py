#En este ejemplo, en lugar de inyectar una dependencia directamente, usamos una fábrica para generar las dependencias de forma más controlada.

# Clase de servicio
class ServicioSaludo:
    def saludar(self):
        return "Hola desde la fábrica!"

# Fábrica de servicios
class FabricaServicioSaludo:
    @staticmethod
    def crear_servicio():
        return ServicioSaludo()

# Clase que utiliza la fábrica para obtener su dependencia
class Cliente:
    def __init__(self, fabrica_servicio):
        self.servicio_saludo = fabrica_servicio.crear_servicio()

    def ejecutar(self):
        return self.servicio_saludo.saludar()

# Usamos la fábrica para crear el servicio
cliente = Cliente(FabricaServicioSaludo)
print(cliente.ejecutar())  # Salida: Hola desde la fábrica!
