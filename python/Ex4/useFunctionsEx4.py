from functionsEx4 import *

print('-------MENU-------',
      '\n[1] Pode votar?:',
      '\n[2] Ver Categoria',
      '\n[3] Pode alistar?:',
      '\n[4] Encerrar')

while True:
    opcao = int(input('\nDigite a opção: '))

    if opcao == 1:
        idade = int(input('Qual a sua idade: '))
        nacionalidade = input('Nacionalidade: ')
        print(podeVotar(idade, nacionalidade))

    elif opcao == 2:
        idade = int(input('Qual a sua idade: '))
        print(categoria(idade))

    elif opcao == 3:
        sexo = input('Qual o seu sexo: ')
        idade = int(input('Qual a sua idade: '))
        print(alistar(sexo, idade))
    
    elif opcao > 4:
        print('Opção inválida!')

    else:
        print('Programa encerrado!')
        break

    