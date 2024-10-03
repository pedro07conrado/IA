from openai import OpenAI


client = OpenAI(
    api_key='sua_key',
) 

response = client.chat.completions.create(
    # Especificando o modelo que quero usar
    model='gpt-3.5-turbo',
    # Enviando um prompt com o papel de usuário comum
    messages=[
        {'role': 'user', 'content': 'Me fale mais sobre o Fiat Elba 1988'},
    ],
)

# Exibindo a mensagem recebida
# Dentro da resposta do "response", exibindo somente a mensagem
print(response['choices'][0]['message']['content'])

