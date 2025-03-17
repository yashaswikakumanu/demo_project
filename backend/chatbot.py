import openai

def chat_with_ai(message):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": message}],
        max_tokens=100
    )
    
    return {"response": response["choices"][0]["message"]["content"]}
