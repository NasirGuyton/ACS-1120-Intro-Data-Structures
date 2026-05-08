from __future__ import division, print_function
import random


class Listogram(list):

    def __init__(self, word_list=None):
        super(Listogram, self).__init__()
        self.types = 0
        self.tokens = 0

        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        index = self.index_of(word)

        if index is not None:
            self[index][1] += count
        else:
            self.append([word, count])
            self.types += 1

        self.tokens += count

    def frequency(self, word):
        index = self.index_of(word)

        if index is not None:
            return self[index][1]

        return 0

    def __contains__(self, word):
        return self.index_of(word) is not None

    def index_of(self, target):
        for index, pair in enumerate(self):
            word = pair[0]

            if word == target:
                return index

        return None

    def sample(self):
        dart = random.randint(1, self.tokens)
        fence = 0

        for word, count in self:
            fence += count

            if dart <= fence:
                return word