from transformers import pipeline

question_answerer = pipeline("question-answering", model="consciousAI/question-answering-roberta-base-s-v2")
print(question_answerer(
    question="What day is it today?",
    context="Three days from now, it will be Wednesday and I will get a haircut.",
))