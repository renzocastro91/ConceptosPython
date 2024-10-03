# Inyección de Dependencias en Python

La **Inyección de dependencias** (Dependency Injection, DI) es un patrón de diseño utilizado para hacer que los componentes de un software sean más flexibles y desacoplados. La idea es separar la creación de las dependencias (objetos o servicios que una clase necesita) de su uso, de manera que esas dependencias puedan ser "inyectadas" desde el exterior.

En lugar de que una clase cree sus dependencias de manera interna, se las proporcionan externamente (a través de un constructor, métodos o atributos). Esto facilita el mantenimiento del código, las pruebas unitarias y permite cambiar las dependencias sin modificar el código de la clase principal.

## Ventajas de la inyección de dependencias:
1. **Desacoplamiento**: Las clases no dependen directamente de las implementaciones de sus dependencias, lo que facilita cambiar componentes sin modificar el código.
2. **Facilidad de pruebas**: Es más fácil hacer pruebas unitarias, ya que puedes inyectar objetos "mock" (simulados) que representen las dependencias.
3. **Flexibilidad**: Puedes cambiar las dependencias en tiempo de ejecución o configuración, mejorando la adaptabilidad del código.
4. **Reutilización de código**: Al desacoplar los componentes, es más fácil reutilizar clases y servicios en diferentes contextos.

## Ejemplo en Python

```python
# Dependencia (clase que será inyectada)
class Motor:
    def encender(self):
        return "Motor encendido"

# Clase principal que depende del motor
class Coche:
    def __init__(self, motor):
        # Inyectamos la dependencia (el motor)
        self.motor = motor

    def arrancar(self):
        return self.motor.encender()

# Inyectamos el objeto Motor al crear el coche
motor = Motor()
mi_coche = Coche(motor)
print(mi_coche.arrancar())
```
## Explicación
`Coche` necesita un `Motor`, pero no lo crea internamente. Se lo pasamos a través del constructor.
Si en el futuro queremos cambiar el motor, simplemente inyectamos uno nuevo sin modificar la clase Coche.

## Conclusión
La inyección de dependencias es una técnica clave para crear software modular y flexible. Nos permite separar las preocupaciones y facilita el mantenimiento y la evolución del código.

Aquí tienes un resumen en formato **Markdown** con los conceptos y ejemplos tocados en cada uno de los niveles (básico, medio y complejo) de **inyección de dependencias** en **Python**:

---

# Inyección de Dependencias en Python - Niveles

## Nivel Básico

### Conceptos Clave:
- **Inyección a través del constructor**: Las dependencias se pasan al inicializar una clase.
- **Inyección a través de métodos**: Las dependencias se pueden inyectar después de crear la instancia usando un método.
- **Inyección opcional**: Se define un valor por defecto para la dependencia si no se inyecta explícitamente.
- **Inyección de múltiples dependencias**: Se gestionan varias dependencias en una clase.

### Ejemplos:
1. **Inyección de dependencias a través del constructor**:
   ```python
   class ServicioSaludo:
       def saludar(self):
           return "Hola!"

   class Cliente:
       def __init__(self, servicio_saludo):
           self.servicio_saludo = servicio_saludo

       def ejecutar(self):
           return self.servicio_saludo.saludar()
   ```

2. **Inyección de dependencias a través de un método**:
   ```python
   class Cliente:
       def set_servicio(self, servicio_saludo):
           self.servicio_saludo = servicio_saludo
   ```

3. **Inyección de dependencias opcional**:
   ```python
   class Cliente:
       def __init__(self, servicio_saludo=None):
           self.servicio_saludo = servicio_saludo or ServicioSaludo()
   ```

4. **Inyección de múltiples dependencias**:
   ```python
   class Cliente:
       def __init__(self, servicio_saludo, servicio_despedida):
           self.servicio_saludo = servicio_saludo
           self.servicio_despedida = servicio_despedida
   ```

---

## Nivel Medio

### Conceptos Clave:
- **Uso de interfaces (Protocolos)**: Las clases implementan un protocolo o "interfaz" para definir los métodos necesarios.
- **Patrón Factory**: Uso de una fábrica para crear instancias de servicios o dependencias.
- **Pruebas unitarias con Mocking**: Uso de `unittest.mock` para simular dependencias en las pruebas unitarias.
- **Aplicaciones modulares**: Separar las dependencias en módulos para un sistema más flexible y extensible.

### Ejemplos:
1. **Inyección con una interfaz (Protocol)**:
   ```python
   from typing import Protocol

   class ServicioSaludo(Protocol):
       def saludar(self) -> str:
           pass
   ```

2. **Inyección a través de una fábrica**:
   ```python
   class FabricaServicioSaludo:
       @staticmethod
       def crear_servicio():
           return ServicioSaludo()
   ```

3. **Pruebas unitarias con mocks**:
   ```python
   from unittest.mock import Mock

   mock_servicio = Mock()
   mock_servicio.saludar.return_value = "Hola mock!"
   ```

4. **Aplicaciones modulares**:
   ```python
   class ModuloSaludo:
       def obtener_saludo(self):
           return "Hola, módulo!"
   ```

---

## Nivel Complejo

### Conceptos Clave:
- **Contenedores IoC (Inversión de Control)**: Uso de un contenedor centralizado que administra las dependencias.
- **Decoradores**: Uso de decoradores para inyectar dependencias de manera automática sin modificar el código de la clase.
- **Inyección en un entorno asíncrono**: Integrar dependencias en flujos `async/await` para operaciones concurrentes.
- **Inyección en un framework web (FastAPI)**: Inyección de dependencias en aplicaciones web usando **FastAPI** y ejecución con **Uvicorn**.

### Ejemplos:

1. **Inyección con un contenedor IoC**:
   ```python
   class ContenedorIoC:
       def registrar(self, nombre, instancia):
           self.servicios[nombre] = instancia
   ```

2. **Decoradores para inyección dinámica**:
   ```python
   def inyectar_servicios(func):
       def wrapper(*args, **kwargs):
           kwargs['servicio'] = ServicioSaludo()
           return func(*args, **kwargs)
       return wrapper
   ```

3. **Inyección en un entorno asíncrono**:
   ```python
   class ServicioSaludoAsync:
       async def saludar(self):
           await asyncio.sleep(1)
           return "Hola desde el servicio asíncrono!"
   ```

4. **Inyección en un framework web (FastAPI) y uso de Uvicorn**:
   - **FastAPI** se usa para gestionar la inyección de dependencias en aplicaciones web.
   - **Uvicorn** es el servidor ASGI que ejecuta la aplicación.
   - Comando para ejecutar la app con Uvicorn:
     ```bash
     uvicorn nombre_del_archivo:app --reload
     ```
   - Ruta que utiliza la inyección de dependencias:
     ```python
     from fastapi import FastAPI, Depends

     app = FastAPI()

     @app.get("/saludo")
     def saludo(servicio_saludo: ServicioSaludo = Depends(obtener_servicio_saludo)):
         return {"mensaje": servicio_saludo.saludar()}
     ```

### Particularidades del nivel complejo:
- Uso de **contenedores IoC** para gestionar dependencias.
- **Decoradores** para modificar el comportamiento dinámicamente.
- Integración con **FastAPI** para inyección de dependencias en aplicaciones web.
- Ejecución de la app usando **Uvicorn** con el comando `uvicorn nombre_del_archivo:app --reload`.

---

Este resumen te proporciona una visión clara y estructurada de los diferentes niveles de complejidad al implementar inyección de dependencias en Python, junto con herramientas avanzadas como **FastAPI** y **Uvicorn**.
