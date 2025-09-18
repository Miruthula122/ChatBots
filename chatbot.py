from openai import OpenAI
client=OpenAI(
    api_key="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",
    base_url= "https://openrouter.ai/api/v1"
)
while True:
    user_input = input("You: ") 
    if user_input.lower() in ["exit", "quit", "bye","see you later"]:
        print("Chatbot: Goodbye!")
        break
    response=client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful and friendly AI assistent."},
            {"role": "user","content": user_input}
        ]
    )
    reply = response.choices[0].message.content.strip()
    print(f"Chatbot: {reply}\n")