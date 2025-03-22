import sys

class Factorial:
    def __init__(self):
        """Constructor de la clase Factorial"""
        pass
        
    def calculate(self, num):
        """
        Calcula el factorial de un número
        
        Args:
            num (int): Número para calcular su factorial
            
        Returns:
            int o None: El factorial del número o None si es negativo
        """
        if num < 0: 
            print(f"Factorial de un número negativo ({num}) no existe")
            return None
        elif num == 0: 
            return 1
        else: 
            fact = 1
            while(num > 1): 
                fact *= num 
                num -= 1
            return fact
            
    def run(self, min, max):
        """
        Calcula los factoriales para todos los números en el rango [min, max]
        
        Args:
            min (int): Límite inferior del rango
            max (int): Límite superior del rango
            
        Returns:
            dict: Diccionario con los factoriales calculados {número: factorial}
        """
        if min > max:
            print(f"El rango {min}-{max} no es válido. El inicio debe ser menor o igual al fin.")
            return {}
            
        resultados = {}
        print(f"Calculando factoriales para el rango {min}-{max}:")
        for num in range(min, max + 1):
            resultado = self.calculate(num)
            if resultado is not None:
                resultados[num] = resultado
                print(f"Factorial {num}! = {resultado}")
                
        return resultados


def procesar_rango(rango_str):
    """
    Procesa una cadena de texto que representa un rango y devuelve los límites
    
    Args:
        rango_str (str): Cadena con formato '5', '4-8', '-10' o '15-'
        
    Returns:
        tuple: Par (inicio, fin) con los límites del rango
    """
    # Establecer valores predeterminados
    limite_inferior_predeterminado = 1
    limite_superior_predeterminado = 60
    
    # Verificar si es un rango (contiene '-')
    if '-' in rango_str:
        partes = rango_str.split('-')
        
        # Caso "-hasta" (sin límite inferior)
        if partes[0] == '':
            try:
                fin = int(partes[1])
                return limite_inferior_predeterminado, fin
            except ValueError:
                print(f"Valor inválido para el límite superior: '{partes[1]}'")
                sys.exit(1)
        
        # Caso "desde-" (sin límite superior)
        elif partes[1] == '':
            try:
                inicio = int(partes[0])
                return inicio, limite_superior_predeterminado
            except ValueError:
                print(f"Valor inválido para el límite inferior: '{partes[0]}'")
                sys.exit(1)
        
        # Caso "desde-hasta" (rango completo)
        else:
            try:
                inicio = int(partes[0])
                fin = int(partes[1])
                return inicio, fin
            except ValueError:
                print("Formato de rango inválido. Use el formato 'inicio-fin', '-fin' o 'inicio-'")
                sys.exit(1)
    else:
        # Si no es un rango, intentar procesar como un único número
        try:
            num = int(rango_str)
            return num, num  # Devolver el mismo número como inicio y fin
        except ValueError:
            print("Entrada inválida. Debe ser un número o un rango 'inicio-fin', '-fin' o 'inicio-'")
            sys.exit(1)


# Programa principal
if __name__ == "__main__":
    # Determinar si se proporcionó un argumento
    if len(sys.argv) < 2:
        # Solicitar el rango al usuario mediante input
        rango_str = input("Ingrese un número o rango (ejemplos: 5, 4-8, -10, 15-): ")
    else:
        # Usar el argumento proporcionado
        rango_str = sys.argv[1]

    # Procesar el rango ingresado
    inicio, fin = procesar_rango(rango_str)
    
    # Crear instancia de la clase Factorial y ejecutar
    factorial = Factorial()
    factorial.run(inicio, fin)