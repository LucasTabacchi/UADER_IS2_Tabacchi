import os
import sys

def es_entero(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

lower = 1
upper = 50

os.system('cls')


args = sys.argv[1:3]  

if len(args) == 1:
    if es_entero(args[0]):
        lower = 1
        upper = int(args[0])
    else:
        print("Error: El argumento debe ser un número entero.")
        sys.exit(1)
elif len(args) == 2:
    if es_entero(args[0]) and es_entero(args[1]):
        lower = int(args[0])
        upper = int(args[1])
    else:
        print("Error: los argumentos deben ser números enteros.")
        sys.exit(1)

if lower > upper:
    print("Error: El primer valor debe ser menor o igual que el segundo.")
    sys.exit(1)

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print('%d ' % num)

