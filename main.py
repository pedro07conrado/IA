from openai import OpenAI


client = OpenAI(
    api_key='sua_key',
) 

stream = client.chat.completions.create(
    # Especificando o modelo que quero usar
    model='gpt-3.5-turbo',
    # Enviando um prompt com o papel de usuário comum
    messages=[
        {'role': 'user', 'content': 'Me fale mais sobre o Fiat Elba 1988'},
    ],
    max_tokens=150,
    #por padrão ela ja vem falsa. coloquei assim para melhorar a experiência do user.
    stream=True,
)
#para exibir a msg em formato stream(a saída da resposta é enviada gradualmente)
# Exibindo a mensagem recebida
# No meu print estou quebrando a msg que recebo e exibindo apenas oq eu quero. 

for chuck in stream: 
    if chuck.choices[0].delta.content is not None:
        print(chuck.choices[0].delta.content, end='')



