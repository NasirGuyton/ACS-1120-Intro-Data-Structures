#!python

import random
import re
from dictogram import Dictogram


def tokenize(text):
    """Split text into clean word tokens."""
    return re.findall(r"\b\w+\b|[.!?]", text)


def build_markov_chain(words):
    """Build a Markov chain from a list of words.

    The chain looks like:
    {
        "a": Dictogram(["dog", "cat", "man"]),
        "dog": Dictogram(["runs", "barks"])
    }
    """
    chain = {}

    for index in range(len(words) - 1):
        current_word = words[index]
        next_word = words[index + 1]

        if current_word not in chain:
            chain[current_word] = Dictogram()

        chain[current_word].add_count(next_word)

    return chain


def random_start_word(words):
    """Choose a reasonable word to start a sentence."""
    sentence_starters = []

    for index, word in enumerate(words):
        if index == 0:
            sentence_starters.append(word)
        elif words[index - 1] in [".", "!", "?"]:
            sentence_starters.append(word)

    if len(sentence_starters) > 0:
        return random.choice(sentence_starters)

    return random.choice(words)


def generate_sentence(chain, words, max_words=15):
    """Generate a sentence using a Markov chain."""
    if len(words) == 0:
        return ""

    current_word = random_start_word(words)
    sentence = [current_word]

    for _ in range(max_words - 1):
        if current_word not in chain:
            break

        next_word = chain[current_word].sample()
        sentence.append(next_word)
        current_word = next_word

        if current_word in [".", "!", "?"]:
            break

    return format_sentence(sentence)


def format_sentence(words):
    """Format generated tokens into a readable sentence."""
    sentence = ""

    for word in words:
        if word in [".", "!", "?"]:
            sentence += word
        elif sentence == "":
            sentence += word
        else:
            sentence += " " + word

    if len(sentence) == 0:
        return ""

    sentence = sentence[0].upper() + sentence[1:]

    if sentence[-1] not in [".", "!", "?"]:
        sentence += "."

    return sentence


def main():
    sample_text = "A man, a plan, a canal: Panama! A dog, a panic in a pagoda!"
    words = tokenize(sample_text)
    chain = build_markov_chain(words)

    print("Tokens:")
    print(words)

    print("\nMarkov chain:")
    for word, next_words in chain.items():
        print(word, "->", next_words)

    print("\nGenerated sentence:")
    print(generate_sentence(chain, words))


if __name__ == "__main__":
    main()