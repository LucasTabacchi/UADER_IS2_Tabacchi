#!/usr/bin/python3
# Autor: [Tabacchi Lucas]
# Fecha: [21/03/2025]
# Descripción: Programa en Python para mostrar todos los números primos dentro de un intervalo

# Definimos los extremos inferior y superior del intervalo
lower = 1
upper = 500

print("Prime numbers between", lower, "and", upper, "are:")

# Recorremos cada número en el rango desde 'lower' hasta 'upper' inclusive
for num in range(lower, upper + 1):
    # Todos los números primos son mayores que 1
    if num > 1:
        # Verificamos si num tiene algún divisor además de 1 y de sí mismo
        for i in range(2, num):
            # Si es divisible, no es primo → salimos del bucle
            if (num % i) == 0:
                break
        else:
            # Si no fue divisible por ningún número → es primo
            print(num)

