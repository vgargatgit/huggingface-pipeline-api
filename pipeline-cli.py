import click
from transformers import pipeline

@click.group()
def cli():
    """A simple CLI group."""
    pass

@click.command()
@click.option('--text', help='Text to classify')
def classify(text):
    """Classifies text as Positive or Negative."""    
    classifier = pipeline("sentiment-analysis")    
    click.echo(classifier(text))

@click.command()
@click.option('--question', help='Question that you want to ask')
@click.option('--context', help='Context for the question')
def qa(question, context):
    """Basic Question Answer"""
    question_answerer = pipeline("question-answering", model="consciousAI/question-answering-roberta-base-s-v2")
    click.echo(question_answerer(
        question=question,
        context=context,
    ))

@click.command()
@click.option('--text', help='Text from which to extract name/entity')
def ner(text):
    """Basic ner"""
    ner = pipeline("ner", grouped_entities=True)
    click.echo(ner(text))

cli.add_command(classify)
cli.add_command(qa)
cli.add_command(ner)

if __name__ == '__main__':
    cli()