from abc import ABC, abstractmethod

# Clase abstracta base
class Factura(ABC):
    def __init__(self, importe):
        self.importe = importe

    @abstractmethod
    def mostrar(self):
        pass

# Subclases concretas según condición impositiva
class FacturaIVAResponsable(Factura):
    def mostrar(self):
        print(f"Factura A - IVA Responsable. Importe: ${self.importe:.2f}")

class FacturaIVANoInscripto(Factura):
    def mostrar(self):
        print(f"Factura C - IVA No Inscripto. Importe: ${self.importe:.2f}")

class FacturaIVAExento(Factura):
    def mostrar(self):
        print(f"Factura E - IVA Exento. Importe: ${self.importe:.2f}")

# Factory para generar facturas según condición impositiva
class FacturaFactory:
    @staticmethod
    def crear_factura(condicion_impositiva, importe):
        if condicion_impositiva == "responsable":
            return FacturaIVAResponsable(importe)
        elif condicion_impositiva == "no_inscripto":
            return FacturaIVANoInscripto(importe)
        elif condicion_impositiva == "exento":
            return FacturaIVAExento(importe)
        else:
            raise ValueError("Condición impositiva no válida")

# Ejemplo de uso
if __name__ == "__main__":
    f1 = FacturaFactory.crear_factura("responsable", 10000)
    f1.mostrar()

    f2 = FacturaFactory.crear_factura("no_inscripto", 8500)
    f2.mostrar()

    f3 = FacturaFactory.crear_factura("exento", 5000)
    f3.mostrar()
