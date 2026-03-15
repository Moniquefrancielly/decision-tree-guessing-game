from tree_builder import build_tree
from node import Node
from collections import deque

# --- Parte 2: DFS (Busca em Profundidade) ---
def dfs_visit(node):
    if node is None:
        return
    
    # Exibe a pergunta ou a resposta final
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

# --- Parte 12 (Opcional): Aprendizado Incremental ---
def aprender_novo_item(node_antigo):
    print("\n[Akinator]: Oh não! Eu errei.")
    novo_item = input("Em que prato ou doce você estava pensando? ")
    pergunta_nova = input(f"Que pergunta diferenciaria '{novo_item}' de '{node_antigo.answer}'? ")
    resposta_correta = input(f"Para '{novo_item}', a resposta a essa pergunta é 's' ou 'n'? ").lower()

    # Guarda o palpite que já existia
    palpite_antigo = node_antigo.answer
    
    # Transforma o nó de resposta em um nó de pergunta
    node_antigo.answer = None
    node_antigo.question = pergunta_nova

    # Cria os novos ramos
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
        confirmacao = input(f"\n[Akinator]: Eu acho que é... {node.answer}! Acertei? (s/n): ").lower()
        if confirmacao == 's':
            print("Ótimo! Ganhei mais uma.")
        else:
            aprender_novo_item(node)
        return

    choice = input(f"\n{node.question} (s/n): ").lower()
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
            print("\nExploração DFS (Caminho Profundo):")
            dfs_visit(arvore)
            print()
        elif opcao == '3':
            print("\nExploração BFS (Nível por Nível):")
            bfs_visit(arvore)
            print()
        elif opcao == '4':
            print("Encerrando... Até logo!")
            break
        else:
            print("Opção inválida.")