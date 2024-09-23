# Dependencia
class ServicioSaludo:
    def saludar(self):
        return "Hola, método!"

# Clase que recibe la dependencia
class Cliente:
    def __init__(self):
        self.servicio_saludo = None

    def set_servicio(self, servicio_saludo):
        self.servicio_saludo = servicio_saludo

    def ejecutar(self):
        return self.servicio_saludo.saludar()

# Inyectamos la dependencia con un method
servicio = ServicioSaludo()
cliente = Cliente()
cliente.set_servicio(servicio)
print(cliente.ejecutar())  # Salida: Hola, method!
