import os
from groq import Groq

API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=API_KEY)

def recommend_recipe(ingredients):

    prompt = f"""
    Recommend a healthy recipe using these ingredients:

    {ingredients}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

