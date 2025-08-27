# PNR_proyecto.py
# Derivado de PNR_sistemis.py
# Acepta esfuerzo en PM y grafica dataset, modelo ajustado y modelo escalado
# Ingeniería de Software II - 2025

import pandas as pd
import numpy as np
import argparse
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# ========================================================
# Funciones de soporte
# ========================================================
def esfuerzo_instantaneo(t, a):
    """Esfuerzo instantáneo PNR para un esfuerzo total K y parámetro a"""
    return 2 * K * a * t * np.exp(-a * t**2)

def esfuerzo_acumulado(t, a):
    """Esfuerzo acumulado"""
    return K * (1 - np.exp(-a * t**2))

# ========================================================
# Programa principal
# ========================================================
if __name__ == "__main__":

    # Argumentos
    ap = argparse.ArgumentParser()
    ap.add_argument("-k", "--esfuerzo", required=True, help="Esfuerzo total del proyecto en PM", type=float)
    args = ap.parse_args()
    Kp = args.esfuerzo

    # Dataset histórico
    t_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])        
    E_data = np.array([8, 21, 25, 30, 25, 24, 17, 15, 11, 6])  
    
    # Calibración
    K = np.sum(E_data)   # esfuerzo total histórico
    print(f"Esfuerzo total histórico: K={K} PM")

    popt, _ = curve_fit(esfuerzo_instantaneo, t_data, E_data, p0=[0.1])
    a_estimada = popt[0]
    print(f"Parámetro a estimado: {a_estimada:.3f}")

    # Grilla de tiempo
    t_fit = np.linspace(min(t_data), max(t_data), 200)

    # Curva del modelo best-fit (con K histórico)
    K = np.sum(E_data)  
    E_fit_hist = esfuerzo_instantaneo(t_fit, a_estimada)

    # Curva con Kp (esfuerzo aceptado como input)
    K = Kp
    E_fit_proy = esfuerzo_instantaneo(t_fit, a_estimada)

    # Gráfico
    plt.scatter(t_data, E_data, label="Datos históricos", color="black")
    plt.plot(t_fit, E_fit_hist, label=f"Modelo ajustado (K={np.sum(E_data):.0f})", color="red")
    plt.plot(t_fit, E_fit_proy, label=f"PNR proyectado (K={Kp:.0f})", color="blue")
    
    plt.xlabel("Tiempo (meses)")
    plt.ylabel("Esfuerzo instantáneo (personas)")
    plt.legend()
    plt.grid(True)
    plt.show()

