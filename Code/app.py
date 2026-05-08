"""Main script, uses other modules to generate sentences."""
from flask import Flask
from dictogram import Dictogram

app = Flask(__name__)

# Build histogram once when the server starts
with open("words.txt", "r", encoding="utf-8") as file:
    words = file.read().split()

hist = Dictogram(words)


def generate_sentence(histogram, length=8):
    words = [histogram.sample() for _ in range(length)]
    return " ".join(words).capitalize() + "."


@app.route("/")
def home():
    """Route that returns a web page containing generated text."""
    sentence = generate_sentence(hist)
    return f"<h1>{sentence}</h1>"


if __name__ == "__main__":
    app.run(debug=True)