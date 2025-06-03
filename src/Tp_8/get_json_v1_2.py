"""
getJason_v1_2.py

Aplicación automatizada de pagos que selecciona la cuenta más adecuada
en función del saldo disponible y balancea entre múltiples tokens (bancos).

Patrones usados:
- Singleton para lectura de JSON
- Chain of Responsibility para ruteo de pagos
- Iterator para listar pagos

Uso:
    python getJason_v1_2.py

Autor: UADER-FCyT-IS2 © 2025
"""

import json
import os
from collections import deque

# -------------------------------
# Singleton para lectura de JSON
# -------------------------------
class JsonReaderSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def load_json(self, path):
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Archivo no encontrado: {path}")
        with open(path, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError as e:
                raise ValueError(f"Error al parsear JSON: {e}")

# ----------------------------
# Clase que representa un pago
# ----------------------------
class Pago:
    def __init__(self, pedido_id, token, monto):
        self.pedido_id = pedido_id
        self.token = token
        self.monto = monto

    def __str__(self):
        return f"Pedido #{self.pedido_id} - Token: {self.token} - Monto: ${self.monto}"

# -------------------------------------------------
# Registro de pagos (Iterator)
# -------------------------------------------------
class RegistroPagos:
    def __init__(self):
        self.pagos = deque()

    def agregar_pago(self, pago):
        self.pagos.append(pago)

    def listar_pagos(self):
        for pago in self.pagos:
            print(pago)

# -----------------------------------------------------------------
# Handler de cuenta (Cadena de responsabilidad)
# -----------------------------------------------------------------
class CuentaPagoHandler:
    def __init__(self, token, saldo_inicial, clave):
        self.token = token
        self.saldo = saldo_inicial
        self.clave = clave
        self.siguiente = None

    def set_siguiente(self, handler):
        self.siguiente = handler

    def procesar_pago(self, pedido_id, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print(f"[{self.token}] Pago procesado para pedido #{pedido_id}, monto: ${monto}")
            return Pago(pedido_id, self.token, monto)
        elif self.siguiente:
            return self.siguiente.procesar_pago(pedido_id, monto)
        else:
            print(f"[{self.token}] Fondos insuficientes para pedido #{pedido_id}")
            return None


# -----------------------------------------------------------------
# Clase principal de la aplicación
# -----------------------------------------------------------------
class ProcesadorPagosApp:
    VERSION = "1.2"

    def __init__(self, path_config):
        self.reader = JsonReaderSingleton()
        self.config = self.reader.load_json(path_config)
        self.registro = RegistroPagos()
        self._crear_cadena_cuentas()

    def _crear_cadena_cuentas(self):
        token1 = self.config.get("token1")
        token2 = self.config.get("token2")

        self.cuenta1 = CuentaPagoHandler("token1", 1000, token1)
        self.cuenta2 = CuentaPagoHandler("token2", 2000, token2)

        # Cadena: cuenta1 → cuenta2
        self.cuenta1.set_siguiente(self.cuenta2)

        self.turno = 0  # alternancia

    def procesar_pedidos(self, pedidos):
        for pedido_id, monto in pedidos:
            cuenta_actual = self.cuenta1 if self.turno % 2 == 0 else self.cuenta2
            pago = cuenta_actual.procesar_pago(pedido_id, monto)
            if pago:
                self.registro.agregar_pago(pago)
                self.turno += 1  # alternar solo si se procesó con éxito

    def mostrar_pagos(self):
        print("\nPagos realizados:")
        self.registro.listar_pagos()

# ---------------------------
# Ejecución simulada
# ---------------------------
def main():
    print("Procesador de Pagos - versión 1.2")
    app = ProcesadorPagosApp("sitedata.json")

    # Simulación de pedidos de pago
    pedidos = [(1, 500), (2, 500), (3, 500), (4, 500), (5, 500)]
    app.procesar_pedidos(pedidos)
    app.mostrar_pagos()

if __name__ == "__main__":
    main()
