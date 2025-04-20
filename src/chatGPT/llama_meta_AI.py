"""
Asistente de LLaMA 3 vía Groq - Cliente de línea de comandos

Este programa implementa un cliente para interactuar con el modelo LLaMA 3 (70B) usando la API de Groq.
Requiere una clave de API configurada en un archivo .env.
"""

import os
import requests
from dotenv import load_dotenv
load_dotenv()

# Importar readline (según sistema operativo)
try:
    import readline  # Linux/macOS
except ImportError:
    import pyreadline3 as readline  # Windows

# Configuración de la API
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama3-70b-8192"

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}


def obtener_entrada_usuario():
    try:
        consulta_usuario = input("You: ")
        readline.add_history(consulta_usuario)
        return consulta_usuario
    except (EOFError, KeyboardInterrupt) as err:
        print(f"\nInterrupción o fin de entrada: {str(err)}")
        return ""


def procesar_consulta(consulta):
    return consulta.strip()


def obtener_respuesta_llama(consulta):
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "Sos un asistente útil, claro y conciso."},
            {"role": "user", "content": "El usuario va a hacer preguntas relacionadas con programación y conceptos técnicos."},
            {"role": "user", "content": consulta}
        ],
        "temperature": 0.7,
        "max_tokens": 2048,
        "top_p": 1
    }

    try:
        response = requests.post(GROQ_API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        respuesta_texto = response.json()["choices"][0]["message"]["content"]
        return respuesta_texto.strip()

    except requests.exceptions.RequestException as e:
        return f"Error al obtener respuesta del modelo LLaMA 3: {str(e)}"


def main():
    print("Asistente LLaMA 3 (Groq) - usá ↑ para recuperar consulta anterior, 'salir' para terminar\n")

    if not GROQ_API_KEY:
        print("❌ Error: GROQ_API_KEY no está definido. Creá un archivo .env con tu clave.")
        return

    while True:
        consulta_usuario = obtener_entrada_usuario()

        if consulta_usuario.lower() == "salir":
            print("Programa finalizado.")
            break

        consulta_procesada = procesar_consulta(consulta_usuario)

        if not consulta_procesada:
            print("⚠️ Entrada vacía. Por favor escribí algo.")
            continue

        respuesta = obtener_respuesta_llama(consulta_procesada)
        print(f"LLaMA: {respuesta}")


if __name__ == "__main__":
    main()
