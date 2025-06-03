import sys
import os
import random
from collections import deque
import ast  # para convertir string a lista

MAX_RANGO = 65535
NUEVO = True

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def obtener_primos_en_rango(inf, sup):
    return [n for n in range(inf, sup + 1) if es_primo(n)]

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_argumentos(args):
    if len(args) != 3:
        raise ValueError("Debe proporcionar exactamente dos argumentos: inicio y fin del rango.")
    try:
        inf = int(args[1])
        sup = int(args[2])
    except ValueError:
        raise ValueError("Ambos argumentos deben ser números enteros válidos.")
    if inf > sup:
        raise ValueError("El límite inferior no puede ser mayor que el superior.")
    if sup > MAX_RANGO:
        raise ValueError(f"El límite superior no puede exceder {MAX_RANGO}.")
    if inf < 0:
        raise ValueError("El límite inferior no puede ser negativo.")
    return inf, sup

class ClassPrimes:
    def __init__(self):
        self.memoria_archivo = "memoria.txt"
        self.memoria = deque(self.cargar_memoria(), maxlen=10)

    def cargar_memoria(self):
        if os.path.exists(self.memoria_archivo):
            with open(self.memoria_archivo, "r") as f:
                try:
                    contenido = f.read().strip()
                    if contenido:
                        return ast.literal_eval(contenido)
                    else:
                        return []
                except:
                    return []
        return []

    def guardar_memoria(self):
        with open(self.memoria_archivo, "w") as f:
            f.write(str(list(self.memoria)))

    def primes(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def obtener_primos_en_rango(self, inf, sup):
        return [n for n in range(inf, sup + 1) if self.primes(n)]

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def validar_argumentos(self, args):
        return validar_argumentos(args)

    def generar_clave_encriptacion(self):
        primos = self.obtener_primos_en_rango(1, 100)
        intentos = 0
        while intentos < 100:  # límite para evitar bucle infinito
            p1, p2 = random.sample(primos, 2)
            par = tuple(sorted((p1, p2)))
            if par not in self.memoria:
                self.memoria.append(par)
                self.guardar_memoria()
                clave = p1 * p2
                print(f"Par generado: {p1}, {p2}")
                print(f"Clave generada: {clave}")
                print(f"Memoria actual de pares: {list(self.memoria)}")
                return clave
            intentos += 1
        raise RuntimeError("No se pudieron generar nuevos pares únicos.")

    def main(self):
        if "--clave" in sys.argv:
            self.generar_clave_encriptacion()
            return

        try:
            inf, sup = self.validar_argumentos(sys.argv)
            self.limpiar_pantalla()
            print(f"[NUEVO] Números primos entre {inf} y {sup} son:\n")
            primos = self.obtener_primos_en_rango(inf, sup)
            print(" ".join(map(str, primos)))
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

def main():
    if NUEVO:
        ClassPrimes().main()
    else:
        try:
            if "--clave" in sys.argv:
                primos = obtener_primos_en_rango(1, 100)
                par = tuple(random.sample(primos, 2))
                print(f"Par generado: {par}")
                print(f"Clave generada: {par[0] * par[1]}")
                return

            inf, sup = validar_argumentos(sys.argv)
            limpiar_pantalla()
            print(f"[VIEJO] Números primos entre {inf} y {sup} son:\n")
            primos = obtener_primos_en_rango(inf, sup)
            print(" ".join(map(str, primos)))
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()

