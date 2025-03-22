import matplotlib.pyplot as plt
import os

def collatz_iterations(n):
    """
    Calcula el número de iteraciones necesarias para que la secuencia de Collatz
    comenzando en n llegue a 1.
    
    Args:
        n (int): Número inicial
        
    Returns:
        int: Número de iteraciones hasta llegar a 1
    """
    if n <= 0:
        raise ValueError("El número inicial debe ser positivo")
    
    iterations = 0
    while n != 1:
        if n % 2 == 0:  # Si n es par
            n = n // 2
        else:  # Si n es impar
            n = 3 * n + 1
        iterations += 1
    
    return iterations

def calculate_collatz_range(start, end):
    """
    Calcula las iteraciones de Collatz para un rango de números
    
    Args:
        start (int): Inicio del rango
        end (int): Fin del rango
        
    Returns:
        tuple: Listas con los números y sus correspondientes iteraciones
    """
    numbers = list(range(start, end + 1))
    iterations = [collatz_iterations(n) for n in numbers]
    
    return numbers, iterations

def plot_collatz_data(numbers, iterations, output_path=None):
    """
    Crea un gráfico de las iteraciones de Collatz
    
    Args:
        numbers (list): Lista de números iniciales
        iterations (list): Lista de iteraciones correspondientes
        output_path (str, optional): Ruta para guardar el gráfico
    """
    plt.figure(figsize=(12, 8))
    plt.scatter(numbers, iterations, s=1, alpha=0.5)
    
    plt.title('Conjetura de Collatz (3n+1)', fontsize=14)
    plt.xlabel('Número inicial (n)', fontsize=12)
    plt.ylabel('Número de iteraciones hasta llegar a 1', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Añadir algunos detalles adicionales
    max_iterations = max(iterations)
    max_index = iterations.index(max_iterations)
    max_number = numbers[max_index]
    
    plt.annotate(f'Máximo: {max_number} → {max_iterations} iteraciones',
                 xy=(max_number, max_iterations),
                 xytext=(max_number + 500, max_iterations),
                 arrowprops=dict(facecolor='red', shrink=0.05, width=1.5),
                 fontsize=10)
    
    if output_path:
        # Asegurar que el directorio existe
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"Gráfico guardado en: {output_path}")
    
    plt.show()

def main():
    # Crear carpeta src si no existe
    os.makedirs("src", exist_ok=True)
    
    # Calcular las iteraciones de Collatz para los números entre 1 y 10000
    print("Calculando iteraciones de Collatz para los números entre 1 y 10000...")
    numbers, iterations = calculate_collatz_range(1, 1000)
    
    # Algunos datos estadísticos
    max_iterations = max(iterations)
    max_index = iterations.index(max_iterations)
    max_number = numbers[max_index]
    
    print(f"Número con más iteraciones: {max_number} con {max_iterations} iteraciones")
    print(f"Promedio de iteraciones: {sum(iterations)/len(iterations):.2f}")
    
    # Generar y guardar el gráfico
    output_path = "src/collatz_graph.png"
    print("Generando gráfico...")
    plot_collatz_data(numbers, iterations, output_path)

if __name__ == "__main__":
    main()