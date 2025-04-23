# Producto
class Avion:
    def __init__(self):
        self.partes = []

    def agregar_parte(self, parte):
        self.partes.append(parte)

    def mostrar_partes(self):
        print("Partes del avión:")
        for parte in self.partes:
            print(f"- {parte}")

# Builder abstracto
class AvionBuilder:
    def reset(self):
        self.avion = Avion()

    def construir_body(self):
        pass

    def construir_turbinas(self):
        pass

    def construir_alas(self):
        pass

    def construir_tren_aterrizaje(self):
        pass

    def obtener_avion(self):
        return self.avion

# Builder concreto
class AvionComercialBuilder(AvionBuilder):
    def __init__(self):
        self.reset()

    def construir_body(self):
        self.avion.agregar_parte("Body de avión comercial")

    def construir_turbinas(self):
        self.avion.agregar_parte("Turbina izquierda")
        self.avion.agregar_parte("Turbina derecha")

    def construir_alas(self):
        self.avion.agregar_parte("Ala izquierda")
        self.avion.agregar_parte("Ala derecha")

    def construir_tren_aterrizaje(self):
        self.avion.agregar_parte("Tren de aterrizaje")

# Director
class IngenieroAeronautico:
    def __init__(self, builder):
        self.builder = builder

    def construir_avion_completo(self):
        self.builder.reset()
        self.builder.construir_body()
        self.builder.construir_turbinas()
        self.builder.construir_alas()
        self.builder.construir_tren_aterrizaje()
        return self.builder.obtener_avion()



# Cliente
builder = AvionComercialBuilder()
director = IngenieroAeronautico(builder)

avion = director.construir_avion_completo()
avion.mostrar_partes()
