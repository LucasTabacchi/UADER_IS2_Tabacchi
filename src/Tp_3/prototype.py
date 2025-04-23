import copy

class AvionPrototype:
    def __init__(self, tipo, capacidad):
        self.tipo = tipo
        self.capacidad = capacidad

    def clonar(self):
        return copy.deepcopy(self)

    def mostrar_info(self):
        print(f"Avión tipo: {self.tipo}, Capacidad: {self.capacidad}")


# Creamos un prototipo
avion_original = AvionPrototype("Comercial", 180)
print("Avión original:")
avion_original.mostrar_info()

# Clonamos el prototipo
avion_clonado = avion_original.clonar()
print("\nPrimer clon:")
avion_clonado.mostrar_info()

# Clonamos el clon
avion_clon_de_clon = avion_clonado.clonar()
print("\nClon del clon:")
avion_clon_de_clon.mostrar_info()
