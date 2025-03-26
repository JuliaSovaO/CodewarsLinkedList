"""
Convert a linked list to a string
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def stringify(node):
    first = node.head
    nodes = []
    while first:
        nodes.append(first.data)
        first = first.next
    nodes.append(first.data)
    return " -> ".join(nodes) if nodes else "None"


print(stringify(Node(0, Node(1, Node(2, Node(3))))))
