"""
Linked Lists - Sorted Insert
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def build_one_two_three():
    node = Node(1)
    current = node
    for i in range(2, 4):
        current.next = Node(i)
        current = current.next
    current.next = None
    return node


def sorted_insert(head, data):
    new_node = Node(data)
    if not head or head.data >= data:
        new_node.next = head
        return new_node
    current = head
    while current.next and current.next.data < data:
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return head


assert (
    sorted_insert(None, 23).data == 23
), "should be able to insert a node on an empty/None list."
assert sorted_insert(None, 23).next == None, "value at index 1 should be None."

assert (
    sorted_insert(build_one_two_three(), 0.5).data == 0.5
), "should be able to insert new node at head of list."
assert (
    sorted_insert(build_one_two_three(), 0.5).next.data == 1
), "value for node at index 1 should be 1."
assert (
    sorted_insert(build_one_two_three(), 0.5).next.next.data == 2
), "value for node at index 2 should be 2."
assert (
    sorted_insert(build_one_two_three(), 0.5).next.next.next.data == 3
), "value for node at index 3 should be 3."
assert (
    sorted_insert(build_one_two_three(), 0.5).next.next.next.next == None
), "value at index 4 should be None."

assert (
    sorted_insert(build_one_two_three(), 1.5).data == 1
), "value for node at index 0 should be 1."
assert (
    sorted_insert(build_one_two_three(), 1.5).next.data == 1.5
), "value for node at index 1 should be 1.5"
assert (
    sorted_insert(build_one_two_three(), 1.5).next.next.data == 2
), "value for node at index 2 should be 2."
assert (
    sorted_insert(build_one_two_three(), 1.5).next.next.next.data == 3
), "value for node at index 3 should be 3."
assert (
    sorted_insert(build_one_two_three(), 1.5).next.next.next.next == None
), "value at index 4 should be None."
