import sys
import random
import re
from collections import Counter


def load_words():
    with open("words.txt") as file:
        words = file.read().splitlines()
    return words


def get_random_words(words, num_words):
    return random.choices(words, k=num_words)




def histogram(source_text):
    """Build a histogram from text or filename."""
    try:
        with open(source_text, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        text = source_text

    words = re.findall(r"\b\w+\b", text.lower())

    hist = {}
    for word in words:
        hist[word] = hist.get(word, 0) + 1

    return hist


def unique_words(hist):
    """Return number of unique words."""
    return len(hist)


def frequency(word, hist):
    """Return frequency of a given word."""
    return hist.get(word.lower(), 0)


def most_frequent(hist):
    max_count = max(hist.values())
    return [word for word, count in hist.items() if count == max_count]


def least_frequent(hist):
    min_count = min(hist.values())
    return [word for word, count in hist.items() if count == min_count]


def mean_frequency(hist):
    return sum(hist.values()) / len(hist)


def median_frequency(hist):
    values = sorted(hist.values())
    n = len(values)

    if n % 2 == 1:
        return values[n // 2]
    else:
        return (values[n // 2 - 1] + values[n // 2]) / 2


def mode_frequency(hist):
    counts = Counter(hist.values())
    return counts.most_common(1)[0][0]




def main():
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        num_words = int(sys.argv[1])

        words = load_words()
        random_words = get_random_words(words, num_words)

        sentence = " ".join(random_words) + "."
        print(sentence)

    else:
        sample_text = "one fish two fish red fish blue fish"

        hist = histogram(sample_text)

        print("Histogram:", hist)
        print("Unique words:", unique_words(hist))
        print("Frequency of 'fish':", frequency("fish", hist))
        print("Most frequent:", most_frequent(hist))
        print("Least frequent:", least_frequent(hist))
        print("Mean:", mean_frequency(hist))
        print("Median:", median_frequency(hist))
        print("Mode:", mode_frequency(hist))


if __name__ == "__main__":
    main()