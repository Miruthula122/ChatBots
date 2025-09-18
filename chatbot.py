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