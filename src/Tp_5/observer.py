class Observer:
    def notificar(self, id_emitido):
        raise NotImplementedError


class ObservadorConcreto(Observer):
    def __init__(self, id_propio):
        self.id_propio = id_propio

    def notificar(self, id_emitido):
        if id_emitido == self.id_propio:
            print(f"Observador con ID '{self.id_propio}' recibió y reconoció el ID '{id_emitido}'")


class Emisor:
    def __init__(self):
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def emitir_id(self, id_emitido):
        print(f"\nEmisor emite ID: '{id_emitido}'")
        for observador in self.observadores:
            observador.notificar(id_emitido)


# Crear emisor
emisor = Emisor()

# Crear y registrar observadores con ID específicos
obs1 = ObservadorConcreto("AB12")
obs2 = ObservadorConcreto("X9Z8")
obs3 = ObservadorConcreto("LMNO")
obs4 = ObservadorConcreto("1234")

emisor.agregar_observador(obs1)
emisor.agregar_observador(obs2)
emisor.agregar_observador(obs3)
emisor.agregar_observador(obs4)

# Emitir 8 IDs (4 de ellos coinciden con los observadores)
ids_a_emitir = ["AB12", "ZZZZ", "X9Z8", "AAAA", "LMNO", "WXYZ", "1234", "QWER"]

for id_emitido in ids_a_emitir:
    emisor.emitir_id(id_emitido)
