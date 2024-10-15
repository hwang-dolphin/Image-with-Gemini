import os
import google.generativeai as genai
import PIL



genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-1.5-flash')

img = PIL.Image.open("eagle.png")

response = model.generate_content(["Write a blog based on this photo.", img])
print(response.text)
