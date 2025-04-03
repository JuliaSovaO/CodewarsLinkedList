"""
Linked Lists - Get Nth Node
"""


class Node(object):
    """Node class for reference"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"Node({self.data}, {self.next})"


def get_nth(node, index):
    terms = []
    head = node
    current = head
    while current:
        terms.append(current.data)
        current = current.next
    return Node(terms[index])


# assert get_nth("1 -> 2 -> 3 -> None", 0).data == 1
# assert get_nth("1 -> 2 -> 3 -> None", 1).data == 2

linked_list = Node(1, Node(2, Node(3, None)))
assert get_nth(linked_list, 0).data == 1, "First node should be located at index 0."
assert get_nth(linked_list, 1).data == 2, "Second node should be located at index 1."
assert get_nth(linked_list, 2).data == 3, "Third node should be located at index 2."
