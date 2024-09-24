# Este ejemplo introduce la herencia de modelos, donde ProductoConDescuento hereda de Producto, añadiendo un campo de descuento
# y una propiedad calculada precio_final, que calcula el precio final aplicando el descuento.

from pydantic import BaseModel


# Modelo básico
class Producto(BaseModel):
    nombre: str
    precio: float


# Modelo que hereda de Producto, añadiendo nuevos campos
class ProductoConDescuento(Producto):
    descuento: float

    # Propiedad calculada: precio con descuento
    @property
    def precio_final(self) -> float:
        return self.precio - (self.precio * self.descuento / 100)


# Crear un producto con descuento
producto = ProductoConDescuento(nombre="Smartphone", precio=1000, descuento=10)
print(f"Precio final:${producto.precio_final}")
