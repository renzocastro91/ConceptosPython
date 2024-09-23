#En aplicaciones modernas, especialmente web, es común trabajar con código asíncrono. Aquí mostramos cómo inyectar dependencias en un flujo asíncrono usando async/await.

import asyncio

# Servicio asíncrono
class ServicioSaludoAsync:
    async def saludar(self):
        await asyncio.sleep(1)  # Simulamos una operación asíncrona
        return "Hola desde el servicio asíncrono!"

# Cliente que consume el servicio asíncrono
class ClienteAsync:
    def __init__(self, servicio_saludo):
        self.servicio_saludo = servicio_saludo

    async def ejecutar(self):
        return await self.servicio_saludo.saludar()

# Inyectamos la dependencia asíncrona
async def main():
    servicio = ServicioSaludoAsync()
    cliente = ClienteAsync(servicio)
    resultado = await cliente.ejecutar()
    print(resultado)

# Ejecutamos el flujo asíncrono
asyncio.run(main())  # Salida: Hola desde el servicio asíncrono!
