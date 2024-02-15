from transformers import pipeline
pipe = pipeline("translation_en_to_fr", model="t5-base")

text = f"""Solar Horizon is an innovative photovoltaic project aimed at harnessing the power of solar energy to create a sustainable and eco-friendly 
solution for energy production. Located in Tarnos, this state-of-the-art solar facility encompasses cutting-edge photovoltaic technology to convert sunlight into electricity efficiently.
The project incorporates the latest advancements in solar cell technology, utilizing high-efficiency photovoltaic EMS to maximize energy conversion and output.
"""
traduction = pipe(text)[0]['translation_text']
print(traduction)
