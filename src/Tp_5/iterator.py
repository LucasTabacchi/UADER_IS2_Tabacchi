class CadenaIterable:
    def __init__(self, cadena):
        self.cadena = cadena

    def iterador_directo(self):
        return CadenaDirectaIterator(self.cadena)

    def iterador_reverso(self):
        return CadenaReversaIterator(self.cadena)


class CadenaDirectaIterator:
    def __init__(self, cadena):
        self.cadena = cadena
        self.posicion = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.posicion >= len(self.cadena):
            raise StopIteration
        caracter = self.cadena[self.posicion]
        self.posicion += 1
        return caracter


class CadenaReversaIterator:
    def __init__(self, cadena):
        self.cadena = cadena
        self.posicion = len(cadena) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.posicion < 0:
            raise StopIteration
        caracter = self.cadena[self.posicion]
        self.posicion -= 1
        return caracter


texto = CadenaIterable("hola")

print("Recorrido directo:")
for c in texto.iterador_directo():
    print(c)

print("Recorrido reverso:")
for c in texto.iterador_reverso():
    print(c)
