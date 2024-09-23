#Aquí usamos la biblioteca unittest.mock para inyectar un "mock" como dependencia en una prueba unitaria. Esto es útil cuando queremos testear una clase sin usar implementaciones reales de sus dependencias.

from unittest.mock import Mock

# Dependencia real
class ServicioSaludo:
    def saludar(self):
        return "Hola real!"

# Clase que depende del servicio
class Cliente:
    def __init__(self, servicio_saludo):
        self.servicio_saludo = servicio_saludo

    def ejecutar(self):
        return self.servicio_saludo.saludar()

# Creamos un mock para simular el comportamiento del servicio
mock_servicio = Mock()
mock_servicio.saludar.return_value = "Hola mock!"

# Inyectamos el mock en lugar del servicio real
cliente = Cliente(mock_servicio)
print(cliente.ejecutar())  # Salida: Hola mock!
