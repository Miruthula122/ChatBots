import openai
openai.api_key= "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"
openai.api_base= "https://openrouter.ai/api/v1"
user_input= input("You: ")
reply= ""
response= openai.ChatCompletion.create(model= "mistralai/mistral-7b-instruct", messages= [{"role": "system","content": "You are expert translator."},{"role":"user","content":"English: Good Moring\n French: Bonjour"}, {"role": "user", "content": f"English: {user_input}\nFrench: "}])
reply= response['choices'][0]['message']['content']
print(f"Chatbot: {reply}\n")