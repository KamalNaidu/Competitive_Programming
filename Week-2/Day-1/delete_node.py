
def delete_node(node):
    """deletes a node from the middle of a linked list"""

    ptr = node.next
    if ptr:
        node.next = ptr.next
        node.value = ptr.value

    else:
        # tail end node, what to do?
        # seemingly only thing to do is raise an Exception
        raise ValueError("Bad input! Can't delete tail node.")