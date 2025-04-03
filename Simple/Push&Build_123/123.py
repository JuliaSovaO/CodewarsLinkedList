"""
Linked Lists - Push & BuildOneTwoThree
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"Node({self.data}, {self.next})"


def push(head, data):
    if isinstance(head, Node):
        prev = head.data
        head.data = data
        head.next = Node(prev)
        return head
    return Node(data)


def build_one_two_three():
    node = Node(1)
    current = node
    for i in range(2, 4):
        current.next = Node(i)
        current = current.next
    current.next = None
    return node


# chained = None
# chained = push(chained, 3)
# chained = push(chained, 2)
# chained = push(chained, 1)
# assert push(chained, 8) == "8 -> 1 -> 2 -> 3 -> None", push(chained, 8)

assert (
    push(None, 1).data == 1
), "Should be able to create a new linked list with push()."
assert (
    push(None, 1).next == None
), "Should be able to create a new linked list with push()."
assert (
    push(Node(1), 2).data == 2
), "Should be able to prepend a node to an existing node."
assert push(Node(1), 2).next.data == 1, push(Node(1), 2).next.data

assert build_one_two_three().data == 1, "Value at index 0 should be 1."
assert build_one_two_three().next.data == 2, build_one_two_three().next.data
assert build_one_two_three().next.next.data == 3, "Value at index 2 should be 3."
assert build_one_two_three().next.next.next == None, "Value at index 3 should be null."
