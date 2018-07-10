def contains_cycle(node):
    """detect a cycle in a singly linked list"""

    # I seem to recall some sort of algorithm which uses two ptrs, one
    # advances quickly, the other advances slowly. If there is no
    # cycle, it comes to an end in n time. If there is a cycle,
    # eventually the fast ptr catches up to the slow ptr and we found a
    # cycle, again proportional to n time.

    slow = node
    while node.next and node.next.next:
        # print("%s: %s->%s" % (n, node.value, node.next))
        slow = slow.next
        node = node.next.next
        if node is slow:
            return True
    return False