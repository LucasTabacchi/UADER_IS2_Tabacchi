from abc import ABC, abstractmethod

# Componente base
class Componente(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def mostrar(self, nivel=0):
        pass

# Hoja
class Pieza(Componente):
    def mostrar(self, nivel=0):
        print("  " * nivel + f"- Pieza: {self.nombre}")

# Compuesto
class Subconjunto(Componente):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.componentes = []

    def agregar(self, componente: Componente):
        self.componentes.append(componente)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"+ Subconjunto: {self.nombre}")
        for componente in self.componentes:
            componente.mostrar(nivel + 1)

# Producto principal
class Producto(Subconjunto):
    def mostrar(self, nivel=0):
        print(f"# Producto Principal: {self.nombre}")
        for componente in self.componentes:
            componente.mostrar(nivel + 1)


if __name__ == "__main__":
    # Crear el producto principal
    producto = Producto("Producto X")

    # Agregar 3 subconjuntos con 4 piezas cada uno
    for i in range(1, 4):
        subconjunto = Subconjunto(f"Subconjunto {i}")
        for j in range(1, 5):
            pieza = Pieza(f"Pieza {i}.{j}")
            subconjunto.agregar(pieza)
        producto.agregar(subconjunto)

    # Mostrar estructura inicial
    print("Estructura inicial del producto:")
    producto.mostrar()

    # Agregar subconjunto opcional con 4 piezas
    subconjunto_extra = Subconjunto("Subconjunto Opcional")
    for k in range(1, 5):
        subconjunto_extra.agregar(Pieza(f"Pieza Extra.{k}"))
    producto.agregar(subconjunto_extra)

    # Mostrar estructura actualizada
    print("\nEstructura con subconjunto adicional:")
    producto.mostrar()
