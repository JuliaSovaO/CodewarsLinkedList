"""
Linked Lists - Remove Duplicates
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head):
    if not head:
        return None
    seen = set()
    current = head
    prev = None
    while current:
        if current.data in seen:
            prev.next = current.next
        else:
            seen.add(current.data)
            prev = current
        current = current.next
    return head


# def build_one_two_three():
#     node = Node(1)
#     current = node
#     for i in range(2, 4):
#         current.next = Node(i)
#         current = current.next
#     current.next = None
#     return node


# def build_one_two_three_four_five_six():
#     node = Node(1)
#     current = node
#     for i in range(2, 7):
#         current.next = Node(i)
#         current = current.next
#     current.next = None
#     return node


assert (
    remove_duplicates(None) == None
), "removing duplicates from None should return None."
assert (
    remove_duplicates(Node(23)).data == 23
), "removing duplicates from linked list consisting of one node should return the node."
# assert (
#     remove_duplicates(build_one_two_three()) == build_one_two_three()
# ), "removing duplicates from a linked list without duplicates node should return the list."
# assert (
#     remove_duplicates(build_one_two_three_four_five_six())
#     == build_one_two_three_four_five_six()
# ), "removing duplicates from linked list without duplicates node should return the list."
# assert remove_duplicates(build_list([1, 2, 2]))== build_list([1, 2]), "should remove the duplicate '2' entries"
# assert remove_duplicates(build_list([1, 1, 1, 1, 1]))== build_list([1]), "should remove the duplicate '1' entries"
# assert remove_duplicates(build_list([1, 2, 3, 3, 4, 4, 5]))== build_list([1, 2, 3, 4, 5]), "should remove the duplicate '3' and '4' entries"
# assert remove_duplicates(build_list([1, 1, 1, 1, 2, 2, 2, 2]))== build_list([1, 2]), "should remove the duplicate '1' and '2' entries"
