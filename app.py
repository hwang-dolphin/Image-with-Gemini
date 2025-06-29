import os

from google import genai
from google.genai import types

import PIL

client = genai.Client(api_key=os.environ.get('GOOGLE_API_KEY'))

img = PIL.Image.open("eagle.png")

response = client.models.generate_content(
    model='gemini-2.5-pro', 
    contents=['Describe the image', img]
)

print(response.text)
