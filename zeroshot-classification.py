from transformers import pipeline

classifier = pipeline("zero-shot-classification")

# Instead of pretained labels, we want to assign labels that model was not trained on
print(classifier(
    "Interest rates are too high currently",
    candidate_labels=["economics", "politics", "business"],
))