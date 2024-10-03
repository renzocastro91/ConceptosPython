# Esquemas de Pydantic

## ¿Qué es Pydantic?

**Pydantic** es una biblioteca de validación y parsing de datos en **Python** que se basa en las anotaciones de tipos introducidas en las versiones modernas del lenguaje. Es utilizada principalmente para:
- **Validar** datos de entrada.
- **Convertir** datos a tipos correctos (parsing).
- **Garantizar la integridad** de los datos al modelar.

### Características principales:
1. **Validación automática**: Pydantic valida automáticamente los tipos de datos según las anotaciones de tipo que definimos.
2. **Conversión implícita**: Si los datos se pueden convertir a los tipos esperados, Pydantic lo hará por ti.
3. **Modelos basados en clases**: Los esquemas o modelos de datos se definen como clases Python utilizando anotaciones de tipo.
4. **Compatibilidad con JSON**: Está optimizado para trabajar con datos JSON, aunque también puede manejar otros formatos.
5. **Integración fácil con frameworks**: Se usa ampliamente en frameworks como **FastAPI** para validar y parsear datos en APIs web.

---

## ¿Qué es un esquema de Pydantic?

Un **esquema de Pydantic** es un modelo que define cómo deben verse los datos de entrada (o salida) de una aplicación. Un esquema se define como una clase que hereda de `BaseModel`, y cada campo dentro de la clase representa un atributo con su tipo de dato y, opcionalmente, sus restricciones.

### Ejemplo básico de esquema:

```python
from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    nombre: str
    edad: int
```

### En este ejemplo, el esquema Usuario espera tres campos:

- `id` (entero)
- `nombre` (cadena de texto)
- `edad` (entero)

- Pydantic validará automáticamente que cualquier dato proporcionado coincida con este esquema.

## Casos de uso de los esquemas de Pydantic
### 1. **Validación de datos en APIs**
En aplicaciones web, como las desarrolladas con FastAPI, Pydantic se utiliza para validar los datos que se envían a través de solicitudes HTTP (por ejemplo, en el cuerpo de una solicitud POST). Al definir los esquemas, la API puede asegurar que los datos recibidos sean correctos y completos antes de procesarlos.

Ejemplo en FastAPI:
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    nombre: str
    precio: float

@app.post("/items/")
async def crear_item(item: Item):
    return item
```
En este ejemplo, el modelo `Item` asegura que cualquier solicitud `POST` enviada a `/items/` debe contener un `nombre` (cadena) y un `precio` (flotante).

## 2. Parsing y conversión de datos
Pydantic no solo valida, sino que también convierte los datos de entrada al tipo correcto si es posible. Por ejemplo, si un valor que debería ser un entero se pasa como cadena (`"25"`), Pydantic intenta convertirlo automáticamente.

Ejemplo de conversión:

```python
class Producto(BaseModel):
    precio: float

producto = Producto(precio="123.45")
print(producto.precio)  # Salida: 123.45 (convertido a float)
```
## 3. Definir restricciones y validaciones personalizadas
Los esquemas de Pydantic permiten definir validaciones personalizadas para cada campo, como valores mínimos, máximos, expresiones regulares, etc.

Ejemplo con restricciones:
```python
from pydantic import BaseModel, Field

class Usuario(BaseModel):
    id: int
    nombre: str
    edad: int = Field(..., gt=0, lt=150)  # La edad debe ser mayor que 0 y menor que 150
```

## 4. Serialización de datos (JSON-friendly)
Pydantic facilita la serialización de modelos a formatos compatibles con JSON, lo que es útil en contextos como APIs RESTful o sistemas de intercambio de datos.

Ejemplo de serialización a JSON:
```python
usuario = Usuario(id=1, nombre="Juan", edad=30)
print(usuario.json())  # Salida: {"id": 1, "nombre": "Juan", "edad": 30}
```

## Ventajas de usar Pydantic

- **Simplicidad**: Definir y validar datos es sencillo, usando solo anotaciones de tipo.
- **Desempeño**: Pydantic es rápido gracias al uso de validaciones escritas en Cython.
- **Integración nativa con FastAPI**: Frameworks modernos como FastAPI dependen fuertemente de Pydantic para la gestión de datos.
- **Error Handling avanzado**: Cuando un dato no cumple con el esquema, Pydantic genera excepciones con mensajes de error claros y detallados.
- **Validaciones personalizadas**: Se pueden agregar fácilmente validaciones personalizadas mediante decoradores o métodos.
- **Manejo de datos anidados**: Pydantic permite definir esquemas complejos que incluyen otros modelos como parte de los campos.

## Validaciones Personalizadas en Pydantic

Pydantic permite definir validaciones personalizadas agregando métodos con el prefijo @validator. Esto permite una lógica de validación más específica o avanzada que la validación automática basada en tipos.

Ejemplo de validación personalizada:
```python
from pydantic import BaseModel, validator

class Usuario(BaseModel):
    nombre: str
    edad: int

    @validator('edad')
    def validar_edad(cls, value):
        if value < 18:
            raise ValueError('El usuario debe ser mayor de edad')
        return value
```
## Esquemas Anidados
Es posible definir esquemas anidados, lo que permite manejar estructuras de datos más complejas, como listas u otros modelos dentro de un modelo principal.

Ejemplo de esquemas anidados:
```python
from typing import List
from pydantic import BaseModel

class Direccion(BaseModel):
    calle: str
    ciudad: str

class Usuario(BaseModel):
    nombre: str
    direcciones: List[Direccion]

direccion = Direccion(calle="Calle 123", ciudad="Madrid")
usuario = Usuario(nombre="Juan", direcciones=[direccion])
print(usuario)
```

# Conclusión
Los esquemas de Pydantic son una herramienta poderosa para definir, validar y convertir datos en Python. Son especialmente útiles en el desarrollo de APIs y sistemas donde la integridad de los datos es clave. Pydantic no solo ayuda a validar datos entrantes, sino que también facilita la serialización de datos, maneja estructuras complejas, y mejora la seguridad y claridad de las aplicaciones.
