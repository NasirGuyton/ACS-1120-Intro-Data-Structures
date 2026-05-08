#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        self.buckets = []

        for i in range(init_size):
            self.buckets.append(LinkedList())

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = []

        for key, val in self.items():
            items.append('{!r}: {!r}'.format(key, val))

        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n + b), because it checks every bucket and entry.
        """
        all_keys = []

        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)

        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n + b), because it checks every bucket and entry.
        """
        all_values = []

        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)

        return all_values

    def items(self):
        """Return a list of all items in this hash table.
        Running time: O(n + b), because it checks every bucket and entry.
        """
        all_items = []

        for bucket in self.buckets:
            all_items.extend(bucket.items())

        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(n + b), because it checks every bucket and entry.
        """
        count = 0

        for bucket in self.buckets:
            count += bucket.length()

        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Average running time: O(1) with good hashing.
        Worst case: O(n) if many keys collide into one bucket.
        """
        bucket = self.buckets[self._bucket_index(key)]
        return bucket.find(lambda item: item[0] == key) is not None

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Average running time: O(1) with good hashing.
        Worst case: O(n) if many keys collide into one bucket.
        """
        bucket = self.buckets[self._bucket_index(key)]
        item = bucket.find(lambda item: item[0] == key)

        if item is not None:
            return item[1]

        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Average running time: O(1) with good hashing.
        Worst case: O(n) if many keys collide into one bucket.
        """
        bucket = self.buckets[self._bucket_index(key)]

        node = bucket.head

        while node is not None:
            if node.data[0] == key:
                node.data = (key, value)
                return

            node = node.next

        bucket.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Average running time: O(1) with good hashing.
        Worst case: O(n) if many keys collide into one bucket.
        """
        bucket = self.buckets[self._bucket_index(key)]
        item = bucket.find(lambda item: item[0] == key)

        if item is not None:
            bucket.delete(item)
            return

        raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()