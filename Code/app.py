"""Main script, uses other modules to generate sentences."""
from flask import Flask
from sample import histogram, sample_weighted

app = Flask(__name__)

with open("words.txt", "r", encoding="utf-8") as file:
    source_text = file.read()

hist = histogram(source_text)


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    word = sample_weighted(hist)
    return f"<h1>{word}</h1>"


if __name__ == "__main__":
    app.run(debug=True)