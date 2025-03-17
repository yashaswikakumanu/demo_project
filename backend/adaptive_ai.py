import json
import openai

def generate_adaptive_recommendations():
    """AI dynamically adjusts recommendations based on health history"""
    try:
        with open("health_logs.json", "r") as file:
            health_data = json.load(file)
    except FileNotFoundError:
        return {"message": "No health data available"}

    user_behavior = "\n".join([f"{entry['date']}: {entry['activity']}" for entry in health_data])

    prompt = f"""
    Based on the user's health activity history, provide an adaptive health plan:
    {user_behavior}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )

    return {"adaptive_recommendations": response["choices"][0]["message"]["content"]}
