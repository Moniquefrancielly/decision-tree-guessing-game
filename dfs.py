
def dfs_visit(node, count=0):

    if node is None:
        return count

    info = node.question if node.question else f"Resposta: {node.answer}"
    print(f" -> {info}", end="")

    count += 1

    count = dfs_visit(node.yes, count)
    count = dfs_visit(node.no, count)

    return count