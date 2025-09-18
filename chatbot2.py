from openai import OpenAI
client=OpenAI(
    api_key="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",
    base_url= "https://openrouter.ai/api/v1"
)

user_input = input("You: ")

reply=""

response=client.chat.completions.create(
    model="mistralai/mistral-7b-instruct",
    messages=[{"role": "system", "content": "You are a helpful assistant"}, {"role": "user", "content": f"{user_input}\nThink step by step."}, {"role": "assistant", "content": reply}]
)

reply = response.choices[0].message.content.strip()
print(f"Chatbot: {reply}\n")