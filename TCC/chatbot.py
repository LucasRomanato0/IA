from openai import OpenAI

client = OpenAI()

class ChatBot():
    def __init__(self):
        self.client = client
    
    def enviar_mensagem(self, mensagem, lMensagens=None):
        if lMensagens is None:
            lMensagens = [
                {
                    "role": "system",
                    "content": "Você é um assistente virtual de gênero neutro chamado bingo. Não precisa começar toda a sua resposta com 'Oi' ou 'Olá'."
                }
            ]
        
        lMensagens.append({"role": "user", "content": mensagem})  # armazena a mensagem do usuário

        # cria uma conversa com o gpt
        resposta = self.client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = lMensagens
        )

        return resposta.choices[0].message.content

    
    def Begin(self):
        print("Para sair digite 'sair'.")

        lMensagens = []
        while True:
            inputUser = input('Você: ')

            if inputUser.lower() == 'sair':
                break
            elif inputUser.lower().__contains__('bingo') == False:
                True
            else:
                resposta = self.enviar_mensagem(inputUser)
                lMensagens.append(resposta) # armazena a mensagem do chatbot
                print('Chatbot: ', resposta)

if __name__ == '__main__':
    # print(sd.query_devices())
    ChatBot().Begin()

# print(enviar_mensagem('Que horas são?'))