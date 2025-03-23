import matplotlib.pyplot as plt

# Datos de ejemplo para el gráfico
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Crear el gráfico de línea
plt.plot(x, y, marker='o', color='blue', linestyle='--')

# Agregar título y etiquetascls
plt.title("Gráfico de Línea - Ejemplo")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Activar la grilla
plt.grid(True)

# Mostrar el gráfico
plt.show()

