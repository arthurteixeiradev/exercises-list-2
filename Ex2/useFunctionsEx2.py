from functionsEx2 import *

cardapio = [['Cachorro-quente',5.00],
            ['X-Salada', 10.00],
            ['X-Bacon', 12.00],
            ['Bauru', 8.00],
            ['Refrigerante', 4.00],
            ['Suco', 6.00]]

print('----------Cardápio----------',
    '\n0 - Cachorro-quente - R$ 5.0',
    '\n1 - X-Salada - R$ 10.0',
    '\n2 - X-Bacon - R$ 12.0',
    '\n3 - Bauru - R$ 8.0',
    '\n4 - Refrigerante - R$ 4.0',
    '\n5 - Suco - R$ 6.0',
    '\n----------------------------')

valorTotalPago = 0
continuar = 'n'
while continuar != 's':
    codigo = int(input('Código do produto: '))

    if codigo < 6:
        qt = int(input('Quantidade: '))
        print(cardapio[codigo][0], '- R$', produto(cardapio, codigo, qt), f'\n{'-'*28}')
        valorTotalPago = valorTotal(valorTotalPago, cardapio, codigo, qt)
    else:
        print('Código do produto inválido!')
    
    continuar = input('Fechar a conta (s ou n)? ')

print('Valor da conta: R$', valorTotalPago)