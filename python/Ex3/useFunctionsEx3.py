from functionsEx3 import *

valorMinimo = float(input('Valor mínimo para a indenização: '))
valorTotalGasto = 0
maiorValorB = 0

while True:
    metragem = float(input('Metragem da casa em m\u00b2: '))
    if metragem == 0:
        break

    classe = input('Classe ("A" ou "B"): ')
    valorCasaAtual = indenizaPropri(valorMinimo, metragem, classe)
    print('Valor a ser pago para esse proprietário: R$', valorCasaAtual)
    valorTotalGasto = valorTotalGasto + valorCasaAtual
    maiorValorB = maiorB(maiorValorB, valorCasaAtual, classe)

print('Valor total gasto pela prefeitura: R$', valorTotalGasto)
print('O maio valor pago uma casa de classe "B": R$', maiorValorB)