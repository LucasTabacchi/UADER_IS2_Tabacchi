class Handler:
    def __init__(self):
        self.next = None

    def set_next(self, handler):
        self.next = handler
        return handler  # permite encadenar con fluidez

    def handle(self, number):
        if self.next:
            return self.next.handle(number)
        else:
            return f"{number} no consumido"

class ParHandler(Handler):
    def handle(self, number):
        if number % 2 == 0:
            return f"{number} consumido por ParHandler"
        return super().handle(number)

class PrimoHandler(Handler):
    def es_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def handle(self, number):
        if self.es_primo(number):
            return f"{number} consumido por PrimoHandler"
        return super().handle(number)

# Crear la cadena de responsabilidad
par_handler = ParHandler()
primo_handler = PrimoHandler()

# Encadenar: primero prueba par, luego primo
par_handler.set_next(primo_handler)

# Procesar los números del 1 al 100
for numero in range(1, 101):
    resultado = par_handler.handle(numero)
    print(resultado)
