from node import Node

def build_tree():
    root = Node(question="É doce?") # a raiz do sistema

    # Parte DOCE (yes)
    doce_gelado = Node(question="É gelado?")
    root.yes = doce_gelado

    # Sub-ramo Gelado
    gelado_sorvete = Node(question="É sorvete?")
    doce_gelado.yes = gelado_sorvete
    gelado_sorvete.yes = Node(answer="Sorvete")
    
    gelado_pave = Node(question="É pavê?")
    gelado_sorvete.no = gelado_pave
    gelado_pave.yes = Node(answer="Pavê")
    gelado_pave.no = Node(answer="Pudim")

    # Sub-ramo não gelado
    tem_chocolate = Node(question="Tem chocolate?")
    doce_gelado.no = tem_chocolate
    
    choc_bolo = Node(question="É bolo?")
    tem_chocolate.yes = choc_bolo
    choc_bolo.yes = Node(answer="Bolo de chocolate")
    
    choc_brigadeiro = Node(question="É brigadeiro?")
    choc_bolo.no = choc_brigadeiro
    choc_brigadeiro.yes = Node(answer="Brigadeiro")
    choc_brigadeiro.no = Node(answer="Sonho")

    # Sub-ramo sem chocolate
    biscoito_doce = Node(question="É biscoito?")
    tem_chocolate.no = biscoito_doce
    biscoito_doce.yes = Node(answer="Biscoito doce")
    
    vai_forno = Node(question="Vai ao forno?")
    biscoito_doce.no = vai_forno
    vai_forno.yes = Node(answer="Tortelete")
    
    festinhas = Node(question="Tem em festinhas?")
    vai_forno.no = festinhas
    festinhas.yes = Node(answer="Beijinho")
    festinhas.no = Node(answer="Doce desconhecido")

    # Parte SALGADO (no)
    frito = Node(question="É frito?")
    root.no = frito

    # Sub-ramo frito
    tem_recheio = Node(question="Tem recheio?")
    frito.yes = tem_recheio
    
    coxinha = Node(question="É coxinha?")
    tem_recheio.yes = coxinha
    coxinha.yes = Node(answer="Coxinha")
    coxinha.no = Node(answer="Pastel")
    tem_recheio.no = Node(answer="Batata frita")

    # Sub-ramo não frito
    tem_pao = Node(question="Tem pão?")
    frito.no = tem_pao
    
    tem_hamburguer = Node(question="Tem hambúrguer?")
    tem_pao.yes = tem_hamburguer
    tem_hamburguer.yes = Node(answer="Hambúrguer")
    tem_hamburguer.no = Node(answer="Passaporte")

    # Sub-ramo sem pão
    polvilho = Node(question="É feito com polvilho?")
    tem_pao.no = polvilho
    polvilho.yes = Node(answer="Pão de queijo")
    
    frigideira = Node(question="É feito na frigideira?")
    polvilho.no = frigideira
    frigideira.yes = Node(answer="Tapioca")

    fatia = Node(question="É servido em fatias?")
    frigideira.no = fatia
    fatia.yes = Node(answer= "Torta")
    fatia.no = Node(answer="Empada")

    return root