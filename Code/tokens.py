#!python

"""
Tokenizer for cleaned corpus text.

Can be used as a module:

    from tokens import tokenize

Or as a script:

    python tokens.py cleaned_corpus.txt
"""

import sys
import re


def remove_extra_punctuation(text):
    """Remove or separate punctuation before tokenizing."""
    # Replace em dashes / double dashes with spaces
    text = re.sub(r"--+", " ", text)

    # Remove punctuation we do not want as tokens
    text = re.sub(r"[,;:()\[\]{}]", "", text)

    return text


def tokenize(text):
    """Convert source text into a list of word/punctuation tokens.

    Keeps sentence-ending punctuation as tokens so the Markov generator
    knows where sentences can stop.
    """
    text = remove_extra_punctuation(text)

    # Match words with optional apostrophes/hyphens, or sentence punctuation
    tokens = re.findall(r"[A-Za-z]+(?:['-][A-Za-z]+)*|[.!?]", text)

    return tokens


def tokenize_file(filename):
    """Read a file and return its tokens."""
    with open(filename, "r", encoding="utf-8") as file:
        source_text = file.read()

    return tokenize(source_text)


def main():
    if len(sys.argv) < 2:
        print("No source text filename given as argument")
        return

    filename = sys.argv[1]
    tokens = tokenize_file(filename)

    print(tokens)


if __name__ == "__main__":
    main()