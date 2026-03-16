from collections import deque

def bfs_visit(root):

    if root is None:
        return 0

    queue = deque([root])
    count = 0

    while queue:

        node = queue.popleft()

        info = node.question if node.question else f"Resposta: {node.answer}"
        print(f" -> {info}", end="")

        count += 1

        if node.yes:
            queue.append(node.yes)

        if node.no:
            queue.append(node.no)

    return count