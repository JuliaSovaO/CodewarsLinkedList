"""
Convert a linked list to a string
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def stringify(node: Node):
    first = node
    nodes = []
    while first:
        nodes.append(str(first.data))
        first = first.next
    nodes.append(str(first))
    return " -> ".join(nodes)


print(stringify(Node(0, Node(1, Node(2, Node(3))))))
