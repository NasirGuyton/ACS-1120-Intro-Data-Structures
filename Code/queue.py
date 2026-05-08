
from linkedlist import LinkedList


class Queue:
    """A first-in, first-out queue."""

    def __init__(self, items=None):
        """Initialize this queue with optional starting items."""
        self.items = LinkedList()

        if items is not None:
            for item in items:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return "Queue({})".format(self.items.items())

    def is_empty(self):
        """Return True if this queue is empty."""
        return self.items.is_empty()

    def enqueue(self, item):
        """Add item to the back of the queue.

        Running time: O(1), because LinkedList has a tail pointer.
        """
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item at the front of the queue.

        Running time: O(1), because we remove from the head.
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")

        front_item = self.items.head.data
        self.items.delete(front_item)
        return front_item

    def length(self):
        """Return the number of items in the queue."""
        return self.items.length()

    def __iter__(self):
        """Iterate through queue items from front to back."""
        node = self.items.head

        while node is not None:
            yield node.data
            node = node.next


def test_queue():
    queue = Queue()

    print(queue)

    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")

    print(queue)

    print(queue.dequeue())
    print(queue)

    queue.enqueue("D")
    print(queue)

    for item in queue:
        print(item)


if __name__ == "__main__":
    test_queue()