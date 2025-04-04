"""
Can you get the loop?
"""


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


def loop_size(node):
    slow = node
    fast = node
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return 0
    loop_length = 1
    current = slow.next
    while current != slow:
        current = current.next
        loop_length += 1
    return loop_length


# node1 = Node()
# node2 = Node()
# node3 = Node()
# node4 = Node()
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node2
# assert loop_size(node1) == 3, "Loop size of 3 expected"

# # Make a longer chain with a loop of 29
# nodes = [Node() for _ in xrange(50)]
# for node, next_node in zip(nodes, nodes[1:]):
#     node.next = next_node
# nodes[49].next = nodes[21]
# assert loop_size(nodes[0]) == 29, "Loop size of 29 expected"

# # Make a very long chain with a loop of 1087
# chain = create_chain(3904, 1087)
# assert loop_size(chain) == 1087, "Loop size of 1087 expected"
