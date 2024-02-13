from transformers import pipeline
classifier = pipeline("zero-shot-classification", model="MoritzLaurer/multilingual-MiniLMv2-L6-mnli-xnli")

sequence_to_classify = "Angela Merkel ist eine Politikerin in Deutschland und Vorsitzende der CDU"
candidate_labels = ["politics", "economy", "entertainment", "environment"]
output = classifier(sequence_to_classify, candidate_labels, multi_label=False)
print(output)


# Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("translation", model="PaulineSanchez/Modele_traduction_HF")