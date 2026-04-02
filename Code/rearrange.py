import sys
import random

def rearrange_words(words):
    shuffled_words = words[:]
    random.shuffle(shuffled_words)
    return shuffled_words

if __name__ == '__main__':
    words = sys.argv[1:]

    if len(words) == 0:
        print("Please provide words as command-line arguments.")
    else:
        shuffled_words = rearrange_words(words)
        print(" ".join(shuffled_words))