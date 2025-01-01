import openai

# Configura tu clave de API
openai.api_key = ""
# Solicitud al modelo usando la nueva interfaz
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Eres un asistente útil."},
        {"role": "user", "content": "¿Cómo funciona la API de OpenAI con Python?"}
    ]
)


# Imprime la respuesta
print(response['choices'][0]['message']['content'])
