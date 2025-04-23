class CalculadoraImpuestos:
    _instance = None  # Atributo para la instancia Singleton

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CalculadoraImpuestos, cls).__new__(cls)
        return cls._instance

    def calcular_total_impuestos(self, base_imponible):
        if base_imponible < 0:
            raise ValueError("La base imponible debe ser un valor positivo")
        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        contribuciones_municipales = base_imponible * 0.012
        return iva + iibb + contribuciones_municipales


calc1 = CalculadoraImpuestos()
calc2 = CalculadoraImpuestos()

base = 1000
impuestos = calc1.calcular_total_impuestos(base)
print(f"Total de impuestos sobre {base}: ${impuestos:.2f}")  # Imprime: Total de impuestos sobre 1000: $272.00
print(calc1 is calc2)  # Imprime True, ambas son la misma instancia
