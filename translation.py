from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
print(translator("Combien de temps faut-il pour apprendre le français?"))