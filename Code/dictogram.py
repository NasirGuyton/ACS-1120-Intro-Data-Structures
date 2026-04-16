from __future__ import division, print_function
import random


class Dictogram(dict):

    def __init__(self, word_list=None):
        super(Dictogram, self).__init__()
        self.types = 0
        self.tokens = 0

        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        if word in self:
            self[word] += count
        else:
            self[word] = count
            self.types += 1
        self.tokens += count

    def frequency(self, word):
        return self.get(word, 0)

    def sample(self):
        dart = random.randint(1, self.tokens)
        fence = 0

        for word, count in self.items():
            fence += count
            if dart <= fence:
                return word