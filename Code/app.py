"""Main script, uses other modules to generate sentences."""

from flask import Flask
from tokens import tokenize
from markov import build_markov_chain, generate_sentence

app = Flask(__name__)


def load_corpus(filename="cleaned_corpus.txt"):
    """Load source text from a corpus file."""
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()



MARKOV_ORDER = 2

corpus_text = load_corpus()
words = tokenize(corpus_text)
chain = build_markov_chain(words, order=MARKOV_ORDER)


@app.route("/")
def home():
    """Route that returns a web page containing generated text."""
    sentence = generate_sentence(chain, max_words=25)
    return f"<h1>{sentence}</h1>"


if __name__ == "__main__":
    app.run(debug=True)