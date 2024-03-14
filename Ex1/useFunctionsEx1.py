from functionsEx1 import *

qtA = 0
qtPessoasDia23_12_22 = 0
qtMaiorTransporte = 0
identMaiorTransporte = ''
while True:
    ident = input('Identificação do ônibus ("A", "B" ou "C"): ')
    if ident == 'X' or ident == 'x':
        break

    dataDaViagem = input('Data da viagem: ')
    qtPass = int(input('Quantidade de passageiros: '))
    valorDaPass = float(input('Valor da passagem: '))
    despesa = float(input('Despesa com a viagem: '))

    print(lucroOrDespesa(qtPass, valorDaPass, despesa))
    qtA = viagensA(ident, qtA)
    qtPessoasDia23_12_22 = qtPessoasDia(ident, dataDaViagem, qtPessoasDia23_12_22, qtPass)

    qtMaiorTransporte, identMaiorTransporte = identMaior(qtPass, qtMaiorTransporte, identMaiorTransporte, ident)

print('A quantidade de viagens realizadas pelo ônibus "A":', qtA)
print('Quantidade de pessoas que viajou no ônibus "B" no dia "23/12/22"', qtPessoasDia23_12_22)
print('Ônibos que transportou a maior quantidade de pessoa em uma viagem:', identMaiorTransporte)