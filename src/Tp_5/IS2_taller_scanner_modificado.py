import os

class State:
    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate

class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate

class Radio:
    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate

        # Definición de memorias M1 a M4: cada una es un dict con 'band' y 'freq'
        self.memories = {
            "M1": {"band": "AM", "freq": "1300"},
            "M2": {"band": "FM", "freq": "88.5"},
            "M3": {"band": "AM", "freq": "1450"},
            "M4": {"band": "FM", "freq": "102.3"},
        }
        # Para barrido por memorias
        self.mem_keys = list(self.memories.keys())
        self.mem_pos = -1

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        # Avanzar en la lista de memorias
        self.mem_pos += 1
        if self.mem_pos == len(self.mem_keys):
            self.mem_pos = 0

        mem = self.memories[self.mem_keys[self.mem_pos]]
        band = mem["band"]
        freq = mem["freq"]

        # Cambiar estado si es necesario
        if band == "AM" and self.state != self.amstate:
            print("Cambiando a AM para memoria {}".format(self.mem_keys[self.mem_pos]))
            self.state = self.amstate
        elif band == "FM" and self.state != self.fmstate:
            print("Cambiando a FM para memoria {}".format(self.mem_keys[self.mem_pos]))
            self.state = self.fmstate

        # Sintonizar frecuencia de la memoria
        print("Sintonizando memoria {}: {} {}".format(self.mem_keys[self.mem_pos], freq, band))

if __name__ == "__main__":
    os.system("clear")
    print("\nCrea un objeto radio y realiza el barrido de memorias M1 a M4")
    radio = Radio()

    # Barrido de 2 ciclos completos de memorias
    for _ in range(len(radio.memories) * 2):
        radio.scan()


