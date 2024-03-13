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

    if ident == 'A':
        qtA = qtA + 1
    
    if ident == 'B' and dataDaViagem == '23/12/22':
        qtPessoasDia23_12_22 = qtPessoasDia23_12_22 + qtPass

    if qtPass > qtMaiorTransporte:
        qtMaiorTransporte = qtPass
        identMaiorTransporte = ident

print('A quantidade de viagens realizadas pelo ônibus "A":', qtA)
print('Quantidade de pessoas que viajou no ônibus "B" no dia "23/12/22"', qtPessoasDia23_12_22)
print('Ônibos que transportou a maior quantidade de pessoa em uma viagem:', identMaiorTransporte)