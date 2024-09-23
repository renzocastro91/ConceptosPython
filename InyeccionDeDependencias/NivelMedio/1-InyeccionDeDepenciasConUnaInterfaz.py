#En Python, podemos utilizar Protocol del módulo typing para definir "interfaces" que otras clases deben implementar. Esto permite mayor flexibilidad en las dependencias.

from typing import Protocol

# Definimos una interfaz para el servicio
class ServicioSaludo(Protocol):
    def saludar(self) -> str:
        pass

# Implementación concreta de la interfaz
class SaludoFormal:
    def saludar(self) -> str:
        return "Buenos días"

# Clase que depende de la interfaz
class Cliente:
    def __init__(self, servicio_saludo: ServicioSaludo):
        self.servicio_saludo = servicio_saludo

    def ejecutar(self):
        return self.servicio_saludo.saludar()

# Inyectamos una clase que implementa la interfaz
servicio = SaludoFormal()
cliente = Cliente(servicio)
print(cliente.ejecutar())  # Salida: Buenos días
