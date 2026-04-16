import requests
from PIL import Image
from io import BytesIO
from google import genai
import os

def describe_image(url):

    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=["Describe this image", img]
    )

    return response.text