# Implementación del "bridge" (la parte de la implementación)
class TrenLaminador:
    def laminar(self, lamina):
        raise NotImplementedError("Este método debe ser implementado por subclases.")

class TrenLaminador5m(TrenLaminador):
    def laminar(self, lamina):
        print(f"Produciendo lámina de 5m x {lamina.ancho}m x {lamina.espesor}\"")

class TrenLaminador10m(TrenLaminador):
    def laminar(self, lamina):
        print(f"Produciendo lámina de 10m x {lamina.ancho}m x {lamina.espesor}\"")

# Abstracción (puede cambiar el tren de laminación libremente)
class Lamina:
    def __init__(self, espesor, ancho, tren_laminador: TrenLaminador):
        self.espesor = espesor
        self.ancho = ancho
        self.tren_laminador = tren_laminador

    def producir(self):
        self.tren_laminador.laminar(self)

    def set_tren_laminador(self, nuevo_tren: TrenLaminador):
        self.tren_laminador = nuevo_tren


if __name__ == "__main__":
    tren5 = TrenLaminador5m()
    tren10 = TrenLaminador10m()

    lamina = Lamina(0.5, 1.5, tren5)
    lamina.producir()  # --> Produciendo lámina de 5m x 1.5m x 0.5"

    # Cambiamos a otro tren de laminado sin modificar la clase Lamina
    lamina.set_tren_laminador(tren10)
    lamina.producir()  # --> Produciendo lámina de 10m x 1.5m x 0.5"

