from transformers import pipeline

generator = pipeline("text-generation")
print(generator("The art of storytelling is"))