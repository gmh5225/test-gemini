
import google.generativeai as genai

genai.configure(api_key=("google api key"))

model = genai.GenerativeModel(model_name = "gemini-pro")

prompt_parts = [
    "Write a Python function and explain it to me",
]

response = model.generate_content(prompt_parts)

print((response.text))




    

