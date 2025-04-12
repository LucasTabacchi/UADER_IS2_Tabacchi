import openai
from openai import OpenAI
import os

# Configurar el cliente de OpenAI
api_key = os.environ.get("OPENAI_API_KEY")  # Mejor usar variables de entorno para las claves API
client = OpenAI(api_key=api_key)

def obtener_entrada_usuario():
    try:
        consulta_usuario = input("You: ")
        return consulta_usuario
    except Exception as e:
        print(f"Error al obtener la entrada: {str(e)}")
        return ""

def procesar_consulta(consulta):
    try:
        if not consulta:
            return "Consulta vacía. Por favor, introduce algo."
        return consulta
    except Exception as e:
        print(f"Error al procesar la consulta: {str(e)}")
        return ""

def obtener_respuesta_chatgpt(consulta):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-instruct",
            messages=[
                {"role": "user", "content": consulta}
            ],
            temperature=1,
            max_tokens=16384,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error al obtener respuesta de ChatGPT: {str(e)}"

def main():
    while True:
        consulta_usuario = obtener_entrada_usuario()
        consulta_procesada = procesar_consulta(consulta_usuario)
        
        if consulta_procesada:
            print(f"You: {consulta_procesada}")
            respuesta = obtener_respuesta_chatgpt(consulta_procesada)
            print(f"chatGPT: {respuesta}")

if __name__ == "__main__":
    main()
