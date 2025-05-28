"""
getJason.py

Programa para extraer valores de claves específicas de un archivo JSON.

Uso:
    python getJason.py <archivo_json> [clave]
    python getJason.py -v

- archivo_json: Ruta al archivo JSON que contiene las claves y valores.
- clave (opcional): Clave cuyo valor se desea obtener. Por defecto es 'token1'.

Copyright UADER-FCyT-IS2©2024 todos los derechos reservados.
"""

import sys
import json
import os

# Cambiá esto para usar la nueva versión (True) o la vieja (False)
use_new_version = True

# --------------------------
# Implementación NUEVA (OO)
# --------------------------
class JsonReaderSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(JsonReaderSingleton, cls).__new__(cls)
        return cls._instance

    def load_json(self, path):
        if not os.path.isfile(path):
            raise ValueError(f"Error: El archivo '{path}' no existe.")
        try:
            with open(path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Error: El archivo '{path}' no contiene un JSON válido.") from exc


class GetJasonAppOO:
    VERSION = "1.1"

    def __init__(self, args):
        self.args = args
        self.reader = JsonReaderSingleton()

    def run(self):
        if len(self.args) == 2 and self.args[1] == '-v':
            print(f"getJason versión {self.VERSION}")
            return

        if len(self.args) < 2:
            print("Uso: python getJason.py <archivo_json> [clave]")
            return

        jsonfile = self.args[1]
        jsonkey = self.args[2] if len(self.args) > 2 else 'token1'

        try:
            data = self.reader.load_json(jsonfile)
            if jsonkey in data:
                print(str(data[jsonkey]))
            else:
                print(f"Error: La clave '{jsonkey}' no se encontró en el archivo JSON.")
        except ValueError as error:
            print(error)

# --------------------------
# Implementación VIEJA
# --------------------------
def run_old_version():
    if len(sys.argv) < 2:
        print("Sin argumentos suficientes, uso: python getJason.py <archivo_json> [clave]")
        sys.exit(1)

    jsonfile = sys.argv[1]
    jsonkey = sys.argv[2] if len(sys.argv) > 2 else 'token1'

    try:
        with open(jsonfile, 'r') as myfile:
            data = myfile.read()
        obj = json.loads(data)
    except FileNotFoundError:
        print(f"Error: El archivo '{jsonfile}' no existe.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: El archivo '{jsonfile}' no contiene un JSON válido.")
        sys.exit(1)

    if jsonkey in obj:
        print(str(obj[jsonkey]))
    else:
        print(f"Error: La clave '{jsonkey}' no se encontró en el archivo JSON.")
        sys.exit(1)

def main():
    if use_new_version:
        app = GetJasonAppOO(sys.argv)
        app.run()
    else:
        run_old_version()

if __name__ == "__main__":
    main()
