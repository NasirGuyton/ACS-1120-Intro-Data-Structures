"""Main script, uses other modules to generate sentences."""

from flask import Flask
from markov import tokenize, build_markov_chain, generate_sentence

app = Flask(__name__)


def load_corpus(filename="corpus.txt"):
    """Load source text from a corpus file."""
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


corpus_text = load_corpus()
words = tokenize(corpus_text)
chain = build_markov_chain(words)


@app.route("/")
def home():
    """Route that returns a web page containing generated text."""
    sentence = generate_sentence(chain, words, max_words=15)
    return f"<h1>{sentence}</h1>"


if __name__ == "__main__":
    app.run(debug=True)