from abc import ABC, abstractmethod

# Componente base
class NumeroBase(ABC):
    @abstractmethod
    def obtener_valor(self):
        pass

# Componente concreto
class Numero(NumeroBase):
    def __init__(self, valor):
        self.valor = valor

    def obtener_valor(self):
        return self.valor

# Decorador base
class NumeroDecorator(NumeroBase):
    def __init__(self, componente: NumeroBase):
        self.componente = componente

# Decoradores concretos
class Suma2(NumeroDecorator):
    def obtener_valor(self):
        return self.componente.obtener_valor() + 2

class Multiplica2(NumeroDecorator):
    def obtener_valor(self):
        return self.componente.obtener_valor() * 2

class Divide3(NumeroDecorator):
    def obtener_valor(self):
        return self.componente.obtener_valor() / 3


if __name__ == "__main__":
    numero_original = Numero(9)
    print("Valor original:", numero_original.obtener_valor())

    # Sumarle 2
    suma = Suma2(numero_original)
    print("Después de sumarle 2:", suma.obtener_valor())

    # Multiplicar por 2
    multi = Multiplica2(numero_original)
    print("Después de multiplicar por 2:", multi.obtener_valor())

    # Dividir por 3
    div = Divide3(numero_original)
    print("Después de dividir por 3:", div.obtener_valor())

    # Anidado: (((9 + 2) * 2) / 3)
    combinado = Divide3(Multiplica2(Suma2(numero_original)))
    print("Resultado de (((9 + 2) * 2) / 3):", combinado.obtener_valor())
