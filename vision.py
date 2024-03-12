import base64
import requests

# Function pour encoder une image en base 64 (aspect purement technique, sans importance)
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Question "métier" 
question = "Quelles non conformités peut on voir sur cette photo de chantier ?"

# OpenAI API Key
api_key = ""

# Chemin vers une photo d'une visite de chantier
image_path = "photos/etancheite.jpg"
base64_image = encode_image(image_path)

# On fait appel à OpenAI pour analyser une photo
headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}
payload = {
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
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300 # paramétrable
}
response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
print(response.json())

# Le resultat (json) pour une seule photo est trés facilement automatisable pour générer le chapitre 
# conformité de chantier dans un compte rendu, directement au format word.

