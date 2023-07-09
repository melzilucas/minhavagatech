import openai

openai.api_key = 'SUA_API_KEY'

def chat_bot(texto):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Suponha que você é um instrutor de programação."},
            {"role": "user", "content": texto},
        ],
        temperature=0.7,
    )
    return response['choices'][0]['message']['content']


while True:
    prompt = input("Digite sua pergunta: ")
    response_chat_gpt = chat_bot(prompt)
    print("ChatBot: ", response_chat_gpt)