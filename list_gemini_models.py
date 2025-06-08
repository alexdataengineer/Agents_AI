import google.generativeai as genai

API_KEY = "AIzaSyB1sZ-elJcnGkwvGA7RUe6lm9z-nbTWMOg"
genai.configure(api_key=API_KEY)

print("Modelos disponíveis e métodos suportados:")
for model in genai.list_models():
    print(f"- {model.name} => {model.supported_generation_methods}") 