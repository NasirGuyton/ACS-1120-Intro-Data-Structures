

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None
        self.tail = None

        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list of all items in this linked list."""
        items = []
        node = self.head

        while node is not None:
            items.append(node.data)
            node = node.next

        return items

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.

        Running time: O(n), because it visits each node once.
        """
        count = 0
        node = self.head

        while node is not None:
            count += 1
            node = node.next

        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.

        Running time: O(1), because tail gives direct access to the end.
        """
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.

        Running time: O(1), because head gives direct access to the front.
        """
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def find(self, matcher):
        """Return the first matching item, or None.

        Supports either:
        - a function, like lambda item: item == 'B'
        - a direct item, like 'B'

        Best case: O(1) if the head matches.
        Worst case: O(n) if the match is near the tail or not present.
        """
        node = self.head

        while node is not None:
            if callable(matcher):
                if matcher(node.data):
                    return node.data
            else:
                if node.data == matcher:
                    return node.data

            node = node.next

        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.

        Best case: O(1) if deleting the head.
        Worst case: O(n) if the item is near the tail or not present.
        """
        previous = None
        node = self.head

        while node is not None:
            if node.data == item:
                if previous is None:
                    self.head = node.next
                else:
                    previous.next = node.next

                if node is self.tail:
                    self.tail = previous

                if self.head is None:
                    self.tail = None

                return

            previous = node
            node = node.next

        raise ValueError('Item not found: {}'.format(item))

    def replace(self, old_item, new_item):
        """Replace old_item with new_item if old_item exists."""
        node = self.head

        while node is not None:
            if node.data == old_item:
                node.data = new_item
                return

            node = node.next


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
