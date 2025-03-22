#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
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

def procesar_rango(rango_str):
    # Verificar si es un rango (contiene '-')
    if '-' in rango_str:
        try:
            inicio, fin = map(int, rango_str.split('-'))
            return inicio, fin
        except ValueError:
            print("Formato de rango inválido. Use el formato 'inicio-fin' (ejemplo: 4-8)")
            sys.exit(1)
    else:
        # Si no es un rango, intentar procesar como un único número
        try:
            num = int(rango_str)
            return num, num  # Devolver el mismo número como inicio y fin
        except ValueError:
            print("Entrada inválida. Debe ser un número o un rango 'inicio-fin'")
            sys.exit(1)

# Determinar si se proporcionó un argumento
if len(sys.argv) < 2:
    # Solicitar el rango al usuario mediante input
    rango_str = input("Ingrese un número o rango (ejemplo: 5 o 4-8): ")
else:
    # Usar el argumento proporcionado
    rango_str = sys.argv[1]

# Procesar el rango ingresado
inicio, fin = procesar_rango(rango_str)

# Verificar que el rango sea válido
if inicio > fin:
    print(f"El rango {inicio}-{fin} no es válido. El inicio debe ser menor o igual al fin.")
    sys.exit(1)

# Calcular y mostrar los factoriales para el rango
print(f"Calculando factoriales para el rango {inicio}-{fin}:")
for num in range(inicio, fin + 1):
    resultado = factorial(num)
    if resultado is not None:
        print(f"Factorial {num}! = {resultado}")

