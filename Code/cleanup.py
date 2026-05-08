#!python

"""
Text cleanup parser for corpus files.

Can be used as a module:

    from cleanup import clean_text

Or as a script:

    python cleanup.py corpus.txt
    python cleanup.py corpus.txt > cleaned_corpus.txt
"""

import sys
import re
import html


CHARS_TO_REMOVE = [
    "_",
    "*",
    "[",
    "]",
    "{",
    "}",
    "<",
    ">",
]

CHARS_TO_REPLACE = {
    "“": '"',
    "”": '"',
    "‘": "'",
    "’": "'",
    "—": " - ",
    "–": " - ",
    "…": "...",
    "\t": " ",
}


def decode_html_entities(text):
    """Convert HTML entities/codes into normal characters."""
    return html.unescape(text)


def normalize_characters(text):
    """Replace smart punctuation with simpler punctuation."""
    for old_char, new_char in CHARS_TO_REPLACE.items():
        text = text.replace(old_char, new_char)

    return text


def remove_unwanted_characters(text):
    """Remove unwanted symbols from text."""
    for char in CHARS_TO_REMOVE:
        text = text.replace(char, "")

    return text


def normalize_whitespace(text):
    """Clean up extra spaces and blank lines."""
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def clean_text(text):
    """Run all cleanup steps on source text."""
    text = decode_html_entities(text)
    text = normalize_characters(text)
    text = remove_unwanted_characters(text)
    text = normalize_whitespace(text)

    return text


def clean_file(filename):
    """Read a file and return cleaned text."""
    with open(filename, "r", encoding="utf-8") as file:
        source_text = file.read()

    return clean_text(source_text)


def main():
    if len(sys.argv) < 2:
        print("Usage: python cleanup.py source.txt [output.txt]")
        return

    input_filename = sys.argv[1]
    cleaned_text = clean_file(input_filename)

    if len(sys.argv) >= 3:
        output_filename = sys.argv[2]

        with open(output_filename, "w", encoding="utf-8") as output_file:
            output_file.write(cleaned_text)

        print("Cleaned text saved to {}".format(output_filename))
    else:
        print(cleaned_text)


if __name__ == "__main__":
    main()