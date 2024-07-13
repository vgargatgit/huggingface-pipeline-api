from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")
print(generator(
    "Radical acceptance begins when",
    max_length=30,
    num_return_sequences=2,
))