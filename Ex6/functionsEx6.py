def verificaEspecie(verteInverte, especie, tipo):
    if verteInverte == 'vertebrado':
        if especie == 'ave':
            if tipo == 'carnivoro':
                return f'Aguia'
            elif tipo == 'onivoro':
                return f'Pomba'
        elif especie == 'mamifero':
            if tipo == 'onivoro':
                return f'Homem'
            elif tipo == 'herbivoro':
                return f'Vaca'
    
    elif verteInverte == 'invertebrado':
        if especie == 'inseto':
            if tipo == 'hematofago':
                return f'Pulga'
            elif tipo == 'herbivoro':
                return f'Lagarta'
        elif especie == 'anelideo':
            if tipo == 'hematofago':
                return f'Sanguessuga'
            elif tipo == 'onivoro':
                return f'Minhoca'

    return f'Não encontrado!!'

