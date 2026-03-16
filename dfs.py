def dfs_visit(node):
    if node is None:
        return 0

    info = node.question if node.question else f"Resposta: {node.answer}"
    print(f" -> {info}", end="")

    count = 1
    count += dfs_visit(node.yes)
    count += dfs_visit(node.no)

    return count