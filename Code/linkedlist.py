def find(self, matcher):
    """Return the first item matching matcher, or None.

    Supports either:
    - a function like lambda item: item == 'B'
    - a direct item like 'B'
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