import sys
import random
import re


def histogram(source_text):
    """Build histogram from text or file."""
    try:
        with open(source_text, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        text = source_text

    words = re.findall(r"\b\w+\b", text.lower())

    hist = {}
    for word in words:
        hist[word] = hist.get(word, 0) + 1

    return hist



def sample_uniform(hist):
    """Return random word (equal probability)."""
    return random.choice(list(hist.keys()))



def sample_weighted(hist):
    """Return random word weighted by frequency."""
    words = list(hist.keys())
    weights = list(hist.values())

    return random.choices(words, weights=weights, k=1)[0]


def main():
    if len(sys.argv) < 2:
        print("Usage: python sample.py <words or filename>")
        return

    input_text = " ".join(sys.argv[1:])
    hist = histogram(input_text)

    print("Uniform sample:", sample_uniform(hist))
    print("Weighted sample:", sample_weighted(hist))


if __name__ == "__main__":
    main()