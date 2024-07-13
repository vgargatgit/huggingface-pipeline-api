from transformers import pipeline

unmasker = pipeline("fill-mask")

# The top_k argument controls how many possibilities you want to be displayed
print(unmasker("This course will teach you all about <mask> models.", top_k=2))