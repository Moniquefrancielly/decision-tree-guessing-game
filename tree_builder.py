from node import Node

def build_tree():
    root = Node(pergunta="É doce?") # a raiz do sistema

    # Parte DOCE do (SIM)
    doce_gelado = Node(pergunta="É gelado?")
    root.sim = doce_gelado

    # Sub-ramo Gelado
    gelado_sorvete = Node(pergunta="É sorvete?")
    doce_gelado.sim = gelado_sorvete
    gelado_sorvete.sim = Node(resposta="Sorvete")
    
    gelado_pave = Node(pergunta="É pavê?")
    gelado_sorvete.nao = gelado_pave
    gelado_pave.sim = Node(resposta="Pavê")
    gelado_pave.nao = Node(resposta="Pudim")

    # Sub-ramo não gelado
    tem_chocolate = Node(pergunta="Tem chocolate?")
    doce_gelado.nao = tem_chocolate
    
    choc_bolo = Node(pergunta="É bolo?")
    tem_chocolate.sim = choc_bolo
    choc_bolo.sim = Node(resposta="Bolo de chocolate")
    
    choc_brigadeiro = Node(pergunta="É brigadeiro?")
    choc_bolo.nao = choc_brigadeiro
    choc_brigadeiro.sim = Node(resposta="Brigadeiro")
    choc_brigadeiro.nao = Node(resposta="Sonho")

    # Sub-ramo sem chocolate
    biscoito_doce = Node(pergunta="É biscoito?")
    tem_chocolate.nao = biscoito_doce
    biscoito_doce.sim = Node(resposta="Biscoito doce")
    
    vai_forno = Node(pergunta="Vai ao forno?")
    biscoito_doce.nao = vai_forno
    vai_forno.sim = Node(resposta="Tortelete")
    
    festinhas = Node(pergunta="Tem em festinhas?")
    vai_forno.nao = festinhas
    festinhas.sim = Node(resposta="Beijinho")
    festinhas.nao = Node(resposta="Doce desconhecido")

    # Parte SALGADO do (NÃO)
    frito = Node(pergunta="É frito?")
    root.nao = frito

    # Sub-ramo frito
    tem_recheio = Node(pergunta="Tem recheio?")
    frito.sim = tem_recheio
    
    coxinha = Node(pergunta="É coxinha?")
    tem_recheio.sim = coxinha
    coxinha.sim = Node(resposta="Coxinha")
    coxinha.nao = Node(resposta="Pastel")
    tem_recheio.nao = Node(resposta="Batata frita")

    # Sub-ramo não frito
    tem_pao = Node(pergunta="Tem pão?")
    frito.nao = tem_pao
    
    tem_hamburguer = Node(pergunta="Tem hambúrguer?")
    tem_pao.sim = tem_hamburguer
    tem_hamburguer.sim = Node(resposta="Hambúrguer")
    tem_hamburguer.nao = Node(resposta="Passaporte") 

    # Sub-ramo sem pão
    polvilho = Node(pergunta="É feito com polvilho?")
    tem_pao.nao = polvilho
    polvilho.sim = Node(resposta="Pão de queijo")
    
    frigideira = Node(pergunta="É feito na frigideira?")
    polvilho.nao = frigideira
    frigideira.sim = Node(resposta="Tapioca")
    frigideira.nao = Node(resposta="Torta")

    return root