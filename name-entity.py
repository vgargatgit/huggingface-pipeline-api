from transformers import pipeline

# We use grouped_entities=True in the pipeline function to combine 
# parts of the sentence that belong to the same entity. 
# Here, the model correctly groups "San" and "Francisco" as 
# a single location, even though it consists of multiple words.

ner = pipeline("ner", grouped_entities=True)
print(ner("San Francisco is on the west coast of USA."))