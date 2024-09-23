#En este ejemplo, hacemos que la dependencia sea opcional. Si no se inyecta, usamos un valor por defecto.

# Dependencia
class ServicioSaludo:
    def saludar(self):
        return "Hola, opcional!"

# Clase con inyección opcional
class Cliente:
    def __init__(self, servicio_saludo=None):
        if servicio_saludo is None:
            self.servicio_saludo = ServicioSaludo()  # Usamos un valor por defecto
        else:
            self.servicio_saludo = servicio_saludo

    def ejecutar(self):
        return self.servicio_saludo.saludar()

# No inyectamos nada, usa la dependencia por defecto
cliente = Cliente()
print(cliente.ejecutar())  # Salida: Hola, opcional!
