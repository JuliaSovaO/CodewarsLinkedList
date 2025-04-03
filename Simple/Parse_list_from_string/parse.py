"""
Parse a linked list from a string
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    # def __str__(self):
    #     return f"Node({self.data}, {self.next})"


def linked_list_from_string(s: str) -> Node:
    nodes = s.replace(" -> None", "").split(" -> ")
    node = Node(nodes[0])
    current = node
    for el in nodes[1:]:
        current.next = Node(el)
        current = current.next
    return node


print(linked_list_from_string("1 -> 2 -> 3 -> None"))
# Node(1, Node(2, Node(3)))
print(linked_list_from_string("0 -> 1 -> 4 -> 9 -> 16 -> None"))
# Node(0, Node(1, Node(4, Node(9, Node(16)))))
