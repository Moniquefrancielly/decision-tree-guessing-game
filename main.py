from tree_builder import build_tree
from collections import deque

# --- Parte 2: DFS (Busca em Profundidade) ---
def dfs_visit(node):
    if node is None:
        return
    info = node.question if node.question else f"Resposta: {node.answer}"
    print(f" -> {info}", end="")
    dfs_visit(node.yes)
    dfs_visit(node.no)

# --- Parte 3: BFS (Busca em Largura) ---
def bfs_visit(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        info = node.question if node.question else f"Resposta: {node.answer}"
        print(f" -> {info}", end="")
        if node.yes:
            queue.append(node.yes)
        if node.no:
            queue.append(node.no)

# --- Parte 4: Simulação do Jogo ---
def play(node):
    if node.answer:
        print(f"\n[Akinator]: Eu acho que é... {node.answer}!")
        return
    choice = input(f"\n{node.question} (s/n): ").lower()
    if choice == 's':
        play(node.yes)
    else:
        play(node.no)

if __name__ == "__main__":
    arvore = build_tree()
    print("\n--- ORDEM DE EXPLORAÇÃO DFS ---")
    dfs_visit(arvore)
    print("\n\n--- ORDEM DE EXPLORAÇÃO BFS ---")
    bfs_visit(arvore)
    print("\n\n--- INICIANDO JOGO ---")
    play(arvore)