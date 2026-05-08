
"""
Performance analysis for histogram count/frequency operations.

Compares:
1. List of tuples histogram
2. Dictogram histogram
3. HashTable histogram
"""

import timeit
from dictogram import Dictogram
from hashtable import HashTable


def make_words(size):
    """Create a predictable list of unique words."""
    words = []

    for number in range(size):
        words.append("word{}".format(number))

    return words




def listogram_index_of(word, histogram):
    """Return index of word in list-of-tuples histogram, or None."""
    for index, pair in enumerate(histogram):
        if pair[0] == word:
            return index

    return None


def make_listogram(words):
    """Build a histogram as a list of tuples."""
    histogram = []

    for word in words:
        index = listogram_index_of(word, histogram)

        if index is None:
            histogram.append((word, 1))
        else:
            old_word, old_count = histogram[index]
            histogram[index] = (old_word, old_count + 1)

    return histogram


def listogram_count(word, histogram):
    """Return frequency count from a list-of-tuples histogram."""
    index = listogram_index_of(word, histogram)

    if index is not None:
        return histogram[index][1]

    return 0



def make_dictogram(words):
    """Build a histogram using the Dictogram class."""
    return Dictogram(words)


def dictogram_count(word, histogram):
    """Return frequency count from a Dictogram."""
    return histogram.frequency(word)




def make_hash_table_histogram(words):
    """Build a histogram using our custom HashTable."""
    histogram = HashTable()

    for word in words:
        if histogram.contains(word):
            current_count = histogram.get(word)
            histogram.set(word, current_count + 1)
        else:
            histogram.set(word, 1)

    return histogram


def hash_table_count(word, histogram):
    """Return frequency count from custom HashTable."""
    try:
        return histogram.get(word)
    except KeyError:
        return 0




def benchmark_count(label, count_function, search_word, histogram, iterations=10000):
    """Benchmark one count function."""
    timer = timeit.Timer(
        lambda: count_function(search_word, histogram)
    )

    result = timer.timeit(number=iterations)

    print("{}: {:.6f} seconds for {:,} lookups".format(
        label,
        result,
        iterations
    ))


def run_benchmarks(size):
    """Build histograms of given size and benchmark count operations."""
    print("\n" + "=" * 60)
    print("Histogram size: {:,} unique words".format(size))
    print("=" * 60)

    words = make_words(size)
    search_word = words[-1]

    list_histogram = make_listogram(words)
    dict_histogram = make_dictogram(words)
    hash_histogram = make_hash_table_histogram(words)

    benchmark_count(
        "List of tuples count - O(n)",
        listogram_count,
        search_word,
        list_histogram
    )

    benchmark_count(
        "Dictogram count - O(1) average",
        dictogram_count,
        search_word,
        dict_histogram
    )

    benchmark_count(
        "HashTable count - O(1) average, O(n) worst case",
        hash_table_count,
        search_word,
        hash_histogram
    )


def print_analysis():
    """Print Big-O analysis summary."""
    print("Performance Analysis")
    print("====================")

    print("\n1. List of tuples")
    print("Count operation: O(n)")
    print("Reason: it must scan through the list until it finds the target word.")

    print("\n2. Dictogram / Python dictionary")
    print("Count operation: O(1) average")
    print("Reason: dictionary lookup uses hashing, so lookup is usually constant time.")

    print("\n3. Custom HashTable")
    print("Count operation: O(1) average, O(n) worst case")
    print("Reason: hash(key) chooses a bucket quickly, but collisions may require scanning a linked list.")


def main():
    print_analysis()

    run_benchmarks(100)
    run_benchmarks(10000)


if __name__ == "__main__":
    main()