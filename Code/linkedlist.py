
class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return "Node({!r})".format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None
        self.tail = None

        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        return "LinkedList({!r})".format(self.items())

    def items(self):
        """Return a list of all items in this linked list."""
        items = []
        node = self.head

        while node is not None:
            items.append(node.data)
            node = node.next

        return items

    def is_empty(self):
        """Return True if this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list."""
        count = 0
        node = self.head

        while node is not None:
            count += 1
            node = node.next

        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list."""
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list."""
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def find(self, matcher):
        """Return an item from this linked list if it is present.

        The matcher argument should be a function that takes an item
        and returns True if it matches.

        Best case running time: O(1), if the first item matches.
        Worst case running time: O(n), if the match is near the end
        or no matching item exists.
        """
        node = self.head

        while node is not None:
            if matcher(node.data):
                return node.data

            node = node.next

        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError."""
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

        raise ValueError("Item not found: {}".format(item))

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
    print(ll)

    for item in ["A", "B", "C"]:
        ll.append(item)
        print(ll)

    print("head:", ll.head)
    print("tail:", ll.tail)
    print("length:", ll.length())

    for item in ["A", "C", "B"]:
        ll.delete(item)
        print(ll)

    print("head:", ll.head)
    print("tail:", ll.tail)
    print("length:", ll.length())


if __name__ == "__main__":
    test_linked_list()