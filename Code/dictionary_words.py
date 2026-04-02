import sys
import random

def load_words():
    with open("words.txt") as file:
        words = file.read().splitlines()
    return words

def get_random_words(words, num_words):
    return random.choices(words, k=num_words)

def main():
    if len(sys.argv) != 2:
        print("Usage: python dictionary_words.py <number>")
        return

    num_words = int(sys.argv[1])

    words = load_words()  
    random_words = get_random_words(words, num_words)

    sentence = " ".join(random_words) + "."
    print(sentence)

if __name__ == "__main__":
    main()