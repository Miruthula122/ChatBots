from openai import OpenAI
client=OpenAI(
    api_key="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",
    base_url= "https://openrouter.ai/api/v1"
)
user_input= input("You: ")
reply= ""
response= client.chat.completions.create(
    model= "gpt-4o-mini", 
    messages= [{"role": "system","content": "You are expert translator."},
               {"role":"user","content":"English: Good Moring\n French: Bonjour"}, 
               {"role": "user", "content": f"English: {user_input}\nFrench: "}]
    )
reply = response.choices[0].message.content.strip()
print(f"Chatbot: {reply}\n")