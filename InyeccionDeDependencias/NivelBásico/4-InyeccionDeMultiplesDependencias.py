#Aquí mostramos cómo se pueden inyectar múltiples dependencias.

# Dependencias
class ServicioSaludo:
    def saludar(self):
        return "Hola!"

class ServicioDespedida:
    def despedirse(self):
        return "Adiós!"

# Clase que recibe múltiples dependencias
class Cliente:
    def __init__(self, servicio_saludo, servicio_despedida):
        self.servicio_saludo = servicio_saludo
        self.servicio_despedida = servicio_despedida

    def ejecutar(self):
        return f"{self.servicio_saludo.saludar()} y {self.servicio_despedida.despedirse()}"

# Inyectamos dos dependencias
saludo = ServicioSaludo()
despedida = ServicioDespedida()
cliente = Cliente(saludo, despedida)
print(cliente.ejecutar())  # Salida: Hola! y Adiós!

