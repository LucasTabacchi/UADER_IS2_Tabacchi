from abc import ABC, abstractmethod

# Producto base
class Hamburguesa:
    def __init__(self, metodo_entrega):
        self.metodo_entrega = metodo_entrega

    def entregar(self):
        self.metodo_entrega.entregar()

# Interfaz para métodos de entrega
class MetodoEntrega(ABC):
    @abstractmethod
    def entregar(self):
        pass

# Implementaciones concretas de los métodos de entrega
class EntregaMostrador(MetodoEntrega):
    def entregar(self):
        print("Hamburguesa entregada en mostrador.")

class RetiroCliente(MetodoEntrega):
    def entregar(self):
        print("Hamburguesa retirada por el cliente.")

class Delivery(MetodoEntrega):
    def entregar(self):
        print("Hamburguesa enviada por delivery.")

# Factory para crear la hamburguesa con el método de entrega correspondiente
class HamburguesaFactory:
    @staticmethod
    def crear_hamburguesa(tipo_entrega):
        if tipo_entrega == "mostrador":
            return Hamburguesa(EntregaMostrador())
        elif tipo_entrega == "retiro":
            return Hamburguesa(RetiroCliente())
        elif tipo_entrega == "delivery":
            return Hamburguesa(Delivery())
        else:
            raise ValueError("Tipo de entrega no válido")

# Ejemplos de uso
if __name__ == "__main__":
    h1 = HamburguesaFactory.crear_hamburguesa("mostrador")
    h1.entregar()

    h2 = HamburguesaFactory.crear_hamburguesa("retiro")
    h2.entregar()

    h3 = HamburguesaFactory.crear_hamburguesa("delivery")
    h3.entregar()




