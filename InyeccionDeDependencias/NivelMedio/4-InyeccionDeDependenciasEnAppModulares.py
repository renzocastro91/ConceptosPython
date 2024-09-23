#Este ejemplo muestra cómo inyectar dependencias en un sistema modular, donde los módulos pueden ser reemplazados o modificados sin cambiar el código principal.

# Módulo de saludo
class ModuloSaludo:
    def obtener_saludo(self):
        return "Hola, módulo!"

# Clase principal que recibe el módulo
class Aplicacion:
    def __init__(self, modulo_saludo):
        self.modulo_saludo = modulo_saludo

    def ejecutar(self):
        return self.modulo_saludo.obtener_saludo()

# Inyectamos un módulo en la aplicación
modulo = ModuloSaludo()
app = Aplicacion(modulo)
print(app.ejecutar())  # Salida: Hola, módulo!

# Podemos cambiar el módulo fácilmente sin tocar la clase Aplicacion
class ModuloSaludoAlternativo:
    def obtener_saludo(self):
        return "Hola, alternativa!"

modulo_alternativo = ModuloSaludoAlternativo()
app = Aplicacion(modulo_alternativo)
print(app.ejecutar())  # Salida: Hola, alternativa!
