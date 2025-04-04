"""
Linked Lists - Recursive Reverse
"""


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


def reverse(head):
    if head is None or head.next is None:
        return head
    rest = reverse(head.next)
    head.next.next = head
    head.next = None
    return rest


# def f():
#     test.assert_equals(reverse(None), None, "should return None if passed in list is None.")

# def f():
#     _list = build_list([1])
#     assert_linked_list_equals(reverse(_list), build_list([1]), "result should be 1 -> None.")

# def f():
#     _list = build_list([1, 3])
#     assert_linked_list_equals(reverse(_list), build_list([3, 1]), "result should be 3 -> 1 -> None.")
#     _list = build_list([3, 1])
#     assert_linked_list_equals(reverse(_list), build_list([1, 3]), "result should be 1 -> 3 -> None.")

# def f():
#     _list = build_list([1, 3, 8])
#     assert_linked_list_equals(reverse(_list), build_list([8, 3, 1]), "result should be 8 -> 3 -> 1 -> None.")
#     _list = build_list([8, 3, 1])
#     assert_linked_list_equals(reverse(_list), build_list([1, 3, 8]), "result should be 1 -> 3 -> 8 -> None.")
#     _list = build_list([1, 8, 3])
#     assert_linked_list_equals(reverse(_list), build_list([3, 8, 1]), "result should be 3 -> 8 -> 1 -> None.")
#     _list = build_list([3, 8, 1])
#     assert_linked_list_equals(reverse(_list), build_list([1, 8, 3]), "result should be 1 -> 8 -> 3 -> None.")

# def f():
#     _list = build_list([1, 3, 5, 7, 9, 11, 13, 15])
#     assert_linked_list_equals(reverse(_list), build_list([15, 13, 11, 9, 7, 5, 3, 1]), "result should be 15 -> 13 -> 11 ... -> 1 -> None.")
#     _list = build_list([15, 13, 11, 9, 7, 5, 3, 1])
#     assert_linked_list_equals(reverse(_list), build_list([1, 3, 5, 7, 9, 11, 13, 15]), "result should be 1 -> 3 -> 5 ... 15 -> None.")
#     _list = build_list([9, 1, 7, 3, 5, 15, 13, 11])
#     assert_linked_list_equals(reverse(_list), build_list([11, 13, 15, 5, 3, 7, 1, 9]), "result should be 11 -> 13 -> 15 -> 5 -> 3 -> 7 -> 1 -> 9 -> None.")
#     _list = build_list([1, 1, 1, 1, 1, 1, 1, 1])
#     assert_linked_list_equals(reverse(_list), build_list([1, 1, 1, 1, 1, 1, 1, 1]), "result should be 1 -> 1 -> 1 -> 1 -> 1 -> 1 -> 1 -> 1 -> None.")

# def f():
#     large_array = build_random_array(500)
#     _list = build_list(list(large_array))
#     large_reversed_array = list(large_array)
#     large_reversed_array.reverse()
#     assert_linked_list_equals(reverse(_list), build_list(large_reversed_array), "result should equal large reversed list.")
