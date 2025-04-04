"""
Swap Node Pairs In Linked List
"""


class Node:
    def __init__(self, next=None):
        self.next = next


def swap_pairs(head):
    if not head or not head.next:
        return head
    prev = None
    current = head

    while current and current.next:
        next_pair = current.next.next
        second = current.next
        second.next = current
        current.next = next_pair
        if prev:
            prev.next = second
        prev = current
        current = next_pair

        if current and current.next:
            current = current.next
    return head


"""
length     original                       expected
------------------------------------------------------------------
  0     ()                             ()
  1     (A)                            (A)
  2     (A --> B)                      (B --> A)
  3     (A --> B --> C)                (B --> A --> C)
  4     (A --> B --> C --> D)          (B --> A --> D --> C)
  5     (A --> B --> C --> D --> E)    (B --> A --> D --> C --> E)
"""
