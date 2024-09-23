# Pasamos un objeto a la clase a través del constructor.

# Dependencia básica
class ServicioSaludo:
    def saludar(self):
        return "Hola!"

# Clase que recibe la dependencia
class Cliente:
    def __init__(self, servicio_saludo):
        self.servicio_saludo = servicio_saludo

    def ejecutar(self):
        return self.servicio_saludo.saludar()

# Inyectamos la dependencia ServicioSaludo
servicio = ServicioSaludo()
cliente = Cliente(servicio)
print(cliente.ejecutar())  # Salida: Hola!
