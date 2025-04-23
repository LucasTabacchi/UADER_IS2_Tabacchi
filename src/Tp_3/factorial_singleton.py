class Factorial:
    _instance = None  # Variable de clase para almacenar la única instancia

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Factorial, cls).__new__(cls)
        return cls._instance

    def calcular(self, n):
        if n < 0:
            raise ValueError("El número debe ser no negativo")
        return 1 if n == 0 else n * self.calcular(n - 1)


f1 = Factorial()
f2 = Factorial()

print(f1.calcular(5))  # Imprime 120
print(f1 is f2)        # Imprime True, ambas variables apuntan a la misma instancia
