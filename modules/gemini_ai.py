import os
from google import genai

def ask_gemini(prompt):
    api_key = os.getenv("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return response.text