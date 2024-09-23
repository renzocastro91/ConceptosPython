#En aplicaciones más grandes, es común usar un contenedor IoC (Inversion of Control) para gestionar las dependencias. Aquí creamos un contenedor IoC básico que administra las instancias de los objetos inyectados.

# Contenedor IoC básico
class ContenedorIoC:
    def __init__(self):
        self.servicios = {}

    def registrar(self, nombre, instancia):
        self.servicios[nombre] = instancia

    def obtener(self, nombre):
        return self.servicios.get(nombre)

# Servicios
class ServicioSaludo:
    def saludar(self):
        return "Hola desde el contenedor IoC!"

class ServicioDespedida:
    def despedirse(self):
        return "Adiós desde el contenedor IoC!"

# Cliente que consume los servicios
class Cliente:
    def __init__(self, saludo, despedida):
        self.saludo = saludo
        self.despedida = despedida

    def ejecutar(self):
        return f"{self.saludo.saludar()} y {self.despedida.despedirse()}"

# Configuramos el contenedor
contenedor = ContenedorIoC()
contenedor.registrar('saludo', ServicioSaludo())
contenedor.registrar('despedida', ServicioDespedida())

# Inyectamos las dependencias desde el contenedor
cliente = Cliente(contenedor.obtener('saludo'), contenedor.obtener('despedida'))
print(cliente.ejecutar())  # Salida: Hola desde el contenedor IoC! y Adiós desde el contenedor IoC!
