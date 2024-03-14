def produto(cardapio, codigo, qt):
    if codigo == 0:
        valor = cardapio[0][1] * qt
        return valor
    elif codigo == 1:
        valor = cardapio[1][1] * qt
        return valor
    elif codigo == 2:
        valor = cardapio[2][1] * qt
        return valor
    elif codigo == 3:
        valor = cardapio[3][1] * qt
        return valor
    elif codigo == 4:
        valor = cardapio[4][1] * qt
        return valor
    else:
        valor = cardapio[5][1] * qt
        return valor

def valorTotal(valorTotalPago, cardapio, codigo, qt):
    valorTotalPago = valorTotalPago + (cardapio[codigo][1] * qt)
    return valorTotalPago

