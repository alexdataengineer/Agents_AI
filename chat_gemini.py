import os
import google.generativeai as genai

# Configuração da chave da API Gemini
# Use a variável de ambiente GEMINI_API_KEY
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Listar e mostrar detalhes dos modelos disponíveis
print("\n=== Modelos Disponíveis na API Gemini ===\n")

# Converter generator para lista
model_list = list(genai.list_models())
available_models = []

print("Listando todos os modelos disponíveis...")
for model in model_list:
    print(f"\nNome: {model.name}")
    print(f"Métodos suportados: {model.supported_generation_methods}")
    if "generateContent" in model.supported_generation_methods:
        available_models.append(model.name)
        print("✓ Suporta generateContent")

print(f"\nTotal de modelos disponíveis: {len(model_list)}")
print(f"Modelos que suportam generateContent: {len(available_models)}")

if not available_models:
    print("\nERRO: Nenhum modelo disponível suporta generateContent.")
    exit(1)

# Tentar usar o primeiro modelo disponível que suporta generateContent
selected_model = None
print("\nTentando inicializar um modelo...")

for model_name in available_models:
    try:
        print(f"\nTentando usar o modelo: {model_name}")
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Olá, você está funcionando?")
        print(f"Modelo {model_name} inicializado com sucesso!")
        selected_model = model
        break
    except Exception as e:
        print(f"Erro ao inicializar {model_name}: {str(e)}")
        continue

if selected_model is None:
    print("\nERRO: Não foi possível inicializar nenhum modelo.")
    exit(1)

# Função de chat
def chat_with_gemini():
    print("Gemini Chat Agent (Digite 'quit' para sair)")
    print("-----------------------------------------")
    
    # Inicializa o modelo Gemini
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    chat = model.start_chat(history=[])

    while True:
        user_input = input("\nVocê: ").strip()
        if user_input.lower() == 'quit':
            print("\nAté logo!")
            break

        try:
            response = chat.send_message(user_input)
            print("\nAI:", response.text)
        except Exception as e:
            print(f"\nErro ao enviar mensagem: {str(e)}")
            print("Tentando novamente na próxima iteração...")

if __name__ == "__main__":
    chat_with_gemini()
