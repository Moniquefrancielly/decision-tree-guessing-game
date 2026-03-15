from tree_builder import build_tree
from node import Node
from collections import deque

# --- Função Auxiliar de Validação ---
def get_valid_input(prompt):
    """Garante que o utilizador responda apenas 's' ou 'n'."""
    while True:
        response = input(prompt).lower().strip()
        if response in ['s', 'n']:
            return response
        print("Resposta inválida! Por favor, digite 's' para Sim ou 'n' para Não.")

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

# --- Parte 12: Aprendizado Incremental ---
def aprender_novo_item(node_antigo):
    print("\n[Akinator]: Oh não! Eu errei.")
    novo_item = input("Em que prato ou doce você estava pensando? ")
    pergunta_nova = input(f"Que pergunta diferenciaria '{novo_item}' de '{node_antigo.answer}'? ")
    
    # Validação aplicada na resposta da nova pergunta
    resposta_correta = get_valid_input(f"Para '{novo_item}', a resposta a essa pergunta é 's' ou 'n'? ")

    palpite_antigo = node_antigo.answer
    node_antigo.answer = None
    node_antigo.question = pergunta_nova

    if resposta_correta == 's':
        node_antigo.yes = Node(answer=novo_item)
        node_antigo.no = Node(answer=palpite_antigo)
    else:
        node_antigo.yes = Node(answer=palpite_antigo)
        node_antigo.no = Node(answer=novo_item)

    print(f"\n[Akinator]: Entendido! Agora sei a diferença entre '{novo_item}' e '{palpite_antigo}'.")

# --- Parte 4: Simulação do Jogo ---
def play(node):
    if node.answer:
        # Validação aplicada no palpite final
        confirmacao = get_valid_input(f"\n[Akinator]: Eu acho que é... {node.answer}! Acertei? (s/n): ")
        if confirmacao == 's':
            print("Ótimo! Ganhei mais uma.")
        else:
            aprender_novo_item(node)
        return

    # Validação aplicada nas perguntas da árvore
    choice = get_valid_input(f"\n{node.question} (s/n): ")
    if choice == 's':
        play(node.yes)
    else:
        play(node.no)

# --- Menu Principal ---
if __name__ == "__main__":
    arvore = build_tree()
    
    while True:
        print("\n" + "="*30)
        print("   AKINATOR GASTRONÔMICO")
        print("="*30)
        print("1. Iniciar Jogo")
        print("2. Ver Ordem de Visita (DFS)")
        print("3. Ver Ordem de Visita (BFS)")
        print("4. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            play(arvore)
        elif opcao == '2':
            print("\nExploração DFS:")
            dfs_visit(arvore)
            print()
        elif opcao == '3':
            print("\nExploração BFS:")
            bfs_visit(arvore)
            print()
        elif opcao == '4':
            print("Encerrando... Até logo!")
            break
        else:
            print("Opção inválida. Escolha entre 1 e 4.")