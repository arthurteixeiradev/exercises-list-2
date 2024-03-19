def indenizaPropri(valorMinimo, metragem, classe):
    if classe == 'A':
        valorPagoPropri = valorMinimo + (metragem * 500)
        return valorPagoPropri
    else:
        valorPagoPropri = valorMinimo + (metragem * 300)
        return valorPagoPropri

def maiorB(maiorValorB, valorCasaAtual, classe):
    if valorCasaAtual > maiorValorB and classe == 'B':
        maiorValorB = valorCasaAtual
        return maiorValorB
    else: 
        return maiorValorB
