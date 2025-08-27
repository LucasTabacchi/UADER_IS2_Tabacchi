#!/usr/bin/env python3
"""Script generado automáticamente para la pregunta 4 del TP9.
Calcula E = 8*S^0.95 y td = 2.4*E^0.33 y grafica los resultados.
Guarda las figuras E_vs_S.png y td_vs_E.png en el mismo directorio.
"""
import numpy as np
import matplotlib.pyplot as plt

def effort(S):
    return 8 * S**0.95

def calendar_td(E):
    return 2.4 * E**0.33

S = np.linspace(0, 10000, 1000)
E_vals = effort(S)

E_range = np.linspace(1, 500, 500)
td_vals = calendar_td(E_range)

plt.plot(S, E_vals)
plt.title("Esfuerzo E vs Tamaño S ( E = 8 * S^0.95 )")
plt.xlabel("Tamaño S")
plt.ylabel("Esfuerzo E")
plt.grid(True)
plt.savefig("E_vs_S.png", dpi=150, bbox_inches="tight")
plt.clf()

plt.plot(E_range, td_vals)
plt.title("Tiempo calendario td vs Esfuerzo E ( td = 2.4 * E^0.33 )")
plt.xlabel("Esfuerzo E")
plt.ylabel("Tiempo calendario td")
plt.grid(True)
plt.savefig("td_vs_E.png", dpi=150, bbox_inches="tight")
