import os
import openai

# Configuração da chave da API OpenAI
# Use a variável de ambiente OPENAI_API_KEY
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = openai.OpenAI(api_key=openai.api_key)

def chat_with_agent():
    print("OpenAI Chat Agent (Digite 'quit' para sair)")
    print("-----------------------------------------")
    history = []

    while True:
        user_input = input("\nVocê: ").strip()
        if user_input.lower() == 'quit':
            print("\nAté logo!")
            break

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=history + [{"role": "user", "content": user_input}]
            )
            print("\nAI:", response.choices[0].message.content)
            history.append({"role": "user", "content": user_input})
            history.append({"role": "assistant", "content": response.choices[0].message.content})
        except Exception as e:
            print(f"\nErro ao enviar mensagem: {str(e)}")
            print("Tentando novamente na próxima iteração...")

if __name__ == "__main__":
    chat_with_agent() 