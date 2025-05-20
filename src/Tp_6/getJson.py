"""
getJason.py

Programa para extraer valores de claves específicas de un archivo JSON.

Uso:
    python getJason.py <archivo_json> [clave]

- archivo_json: Ruta al archivo JSON que contiene las claves y valores.
- clave (opcional): Clave cuyo valor se desea obtener. Por defecto es 'token1'.

Ejemplo:
    python getJason.py sitedata.json token2

Salida:
    Imprime el valor asociado a la clave especificada en el archivo JSON.
"""

import json
import sys

def main():
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

if __name__ == "__main__":
    main()
