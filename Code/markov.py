
import random
from tokens import tokenize
from dictogram import Dictogram
from queue import Queue



def build_markov_chain(words, order=2):
    """Build an nth-order Markov chain.

    For order=1:
    {
        ("the",): Dictogram(["cat", "dog"])
    }

    For order=2:
    {
        ("the", "cat"): Dictogram(["sat", "ran"])
    }

    Each key is a tuple of previous words.
    Each value is a Dictogram of possible next words.
    """
    if order < 1:
        raise ValueError("Order must be at least 1")

    chain = {}

    if len(words) <= order:
        return chain

    previous_words = Queue()

    for index in range(order):
        previous_words.enqueue(words[index])

    for index in range(order, len(words)):
        state = tuple(previous_words)
        next_word = words[index]

        if state not in chain:
            chain[state] = Dictogram()

        chain[state].add_count(next_word)

        previous_words.dequeue()
        previous_words.enqueue(next_word)

    return chain


def get_sentence_start_states(chain):
    """Return states that look like good sentence starters."""
    starters = []

    for state in chain.keys():
        first_word = state[0]

        if first_word and first_word[0].isupper():
            starters.append(state)

    if len(starters) == 0:
        starters = list(chain.keys())

    return starters


def generate_sentence(chain, max_words=20):
    """Generate a sentence using an nth-order Markov chain."""
    if len(chain) == 0:
        return ""

    starters = get_sentence_start_states(chain)
    state = random.choice(starters)

    sentence = list(state)

    for _ in range(max_words - len(sentence)):
        if state not in chain:
            break

        next_word = chain[state].sample()
        sentence.append(next_word)

        if next_word in [".", "!", "?"]:
            break

        state = tuple(list(state[1:]) + [next_word])

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


def print_chain(chain):
    """Print a readable version of the Markov chain."""
    for state, next_words in chain.items():
        print(state, "->", next_words)


def main():
    sample_text = "I went left, you went right, I went left, I went right,"
    words = tokenize(sample_text)

    print("Tokens:")
    print(words)

    print("\nFirst-order Markov chain:")
    first_order_chain = build_markov_chain(words, order=1)
    print_chain(first_order_chain)

    print("\nSecond-order Markov chain:")
    second_order_chain = build_markov_chain(words, order=2)
    print_chain(second_order_chain)

    print("\nGenerated sentence:")
    print(generate_sentence(second_order_chain, max_words=12))


if __name__ == "__main__":
    main()