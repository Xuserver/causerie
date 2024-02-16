import base64
import os
import requests


# OpenAI API Key
api_key = ""
 
class NaldeoVisionModel():
  def __init__(self,image_path=""):
    self.headers = {  
      "Content-Type": "application/json",
      "Authorization": f"Bearer {api_key}"
    }

    # Getting the base64 string
    if not image_path=="" : 
      self.image_path = image_path
      self.load(self.image_path)

  # Function to encode the image
  def encode_image(self,image_path):
    with open(image_path, "rb") as image_file:
      return base64.b64encode(image_file.read()).decode('utf-8')
    
  def load(self,image_path):
    self.image_path = image_path
    if os.path.isfile(image_path):
      self.base64_image = self.encode_image(image_path)
    else:
      print("no file found")
    
  def do(self,question):
    print(f"\nAnalyse de l'image {self.image_path}")
    self.payload = {
      "model": "gpt-4-vision-preview",
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": question
            },
            {
              "type": "image_url",
              "image_url": {
                "url": f"data:image/jpeg;base64,{self.base64_image}"
              }
            }
          ]
        }
      ],
      "max_tokens": 1000
    }
    self.response = requests.post("https://api.openai.com/v1/chat/completions", headers=self.headers, json=self.payload).json()
    return self.response['choices'][0]['message']['content']


vision = NaldeoVisionModel("photos/vannes.jpg")
print(vision.do("Quels équipements voit-on sur la photo et quel est leur état ?"))
vision.load("photos/css.jpg")
print(vision.do("De quel langage s'agit-il ?"))
