"""
Linked Lists - Move Node
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"Node({self.data}, {self.next})"


class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest


def move_node(source, dest):
    source_new = source.split(" -> ")
    dest_new = dest.split(" -> ")
    dest_new.insert(0, source_new[0])
    del source_new[0]
    source_new = " -> ".join(source_new)
    dest_new = " -> ".join(dest_new)
    return Context(source_new, dest_new)


# source = "1 -> 2 -> 3 -> None"
# dest = "4 -> 5 -> 6 -> None"

source = Node(1)
source.next = Node(2)
source.next.next = Node(3)
dest = Node(4)
dest.next = Node(5)
dest.next.next = Node(6)
assert move_node(source, dest).source == "2 -> 3 -> None"
assert move_node(source, dest).dest == "1 -> 4 -> 5 -> 6 -> None"
