import openai
# Configura tu clave de API
openai.api_key = ""
# Solicitud al modelo usando la nueva interfaz
respuesta = openai.ChatCompletion.create(
    modelo="gpt-3.5-turbo",
    mensajes=[
        {"role": "system", "content": "Eres un asistente útil."},
        {"role": "user", "content": "¿Cómo funciona la API de OpenAI con Python?"}
    ]
)
# Imprime la respuesta
print(respuesta['choices'][0]['message']['content'])
