def tree_height(node):

    if node is None:
        return 0

    left = tree_height(node.yes)
    right = tree_height(node.no)

    return max(left, right) + 1


def count_nodes(node):

    if node is None:
        return 0

    return 1 + count_nodes(node.yes) + count_nodes(node.no)


def count_leaves(node):

    if node is None:
        return 0

    if node.answer:
        return 1

    return count_leaves(node.yes) + count_leaves(node.no)
