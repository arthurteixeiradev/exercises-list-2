from functionsEx5 import *

salario = float(input('Valor do salário mínimo: '))
totalGastoPg = 0
menorQt = 9**99
maiorQt = 0
menorVendedor = ''
while True:
    
    nome = input('Qual é o seu nome: ')
    if nome.lower() == 'sair':
        break

    qtCamiseta = int(input('Quantidade de camisetas vendidas: '))
    print(calcular(nome, salario, qtCamiseta))
    totalGastoPg = totalGastoPg + totalGasto(qtCamiseta, salario)
    if qtCamiseta < menorQt:
        menorQt = qtCamiseta
        menorVendedor = nome
    if qtCamiseta > maiorQt:
        maiorQt = qtCamiseta

print('-'*60, '\nTotal gasto com pagamento dos vendedores: R$', totalGastoPg, '\nMenor vendedor:', menorVendedor, '\nMaior número de camisetas vendidas:', maiorQt, '\n', '-'*60)