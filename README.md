Questão 1
→ Utilize a estrutura de repetição while e não utilize lista.
Uma empresa de transporte faz o controle das suas viagens anotando em uma ficha os seguintes dados:
identificação do ônibus (‘A’, ‘B’ ou ‘C’), data da viagem (string), quantidade de passageiros, valor da passagem
e a despesa com a viagem.

Construa um algoritmo que:
Leia os dados das viagens, sendo que a leitura deverá ser encerrada quando a identificação do ônibus for ‘X’
(flag).

* Para a data da viagem, considere que o usuário digitará uma data no formato dd/mm/aa.
Calcule e apresente:
a. Para cada viagem, o ônibus, a data e uma das seguintes mensagens: “Houve lucro”, “Houve prejuízo"
ou “A viagem se pagou”;
b. A quantidade de viagens realizadas pelo ônibus ‘A’;
c. Quantidade de pessoas que viajou no ônibus ‘B’ no dia ‘23/12/22';
d. A identificação do ônibus que transportou a maior quantidade de pessoas em uma viagem.
* Considere que não houve empate.


Questão 2
→ O programa deve funcionar adequadamente se forem alterados os valores ou se forem inseridos ou
retirados itens do cardápio.
A tabela a seguir apresenta o cardápio de um food truck:

O código a seguir cria uma lista que representa o cardápio apresentado, em que são armazenados os nomes e
os valores dos itens oferecidos. A posição (linha) do item no cardápio corresponde ao código dele.
cardapio = [['Cachorro-quente',5.00],
            ['X-Salada', 10.00],
            ['X-Bacon', 12.00],
            ['Bauru', 8.00],
            ['Refrigerante', 4.00],
            ['Suco, 6.00']]

Continue o programa imprimindo o cardápio conforme o modelo (imprimir igual) a seguir:
-----Cardápio-----
Cachorro-quente - R$ 5.0
X-Salada - R$ 10.0
X-Bacon - R$ 12.0
Bauru - R$ 8.0
Refrigerante - R$ 4.0
Suco - R$ 6.0

Depois, leia o código do item e a quantidade deste item para os pedidos de um cliente, de forma que para
cada pedido deve ser apresentado o nome do produto e o valor do pedido. Caso o código digitado seja
inválido, deve ser apresentada uma mensagem ao usuário e nada deve ser calculado para o pedido em

questão. Ao final de cada pedido realizado é perguntado se a conta deve ser fechada e, caso o usuário digite
‘sim’, os pedidos devem ser encerrados e deve ser apresentado o valor total da conta.

Exemplo de execução:
Código do produto:9
Código do produto inválido!
Fechar a conta [s ou n]?n
Código do produto:2
Quantidade:2
X-Bacon - 24.0
Fechar a conta [s ou n]?n
Código do produto:3
Quantidade:5
Bauru - 40.0
Fechar a conta [s ou n]?s
Valor da conta: 64.0


Questão 3
Uma empresa foi contratada pela prefeitura de uma cidade para avaliar a indenização que será dada aos
proprietários de casas que serão derrubadas para a construção de um hospital. Sabendo que o valor da
indenização de cada casa é calculado a partir de um valor mínimo inicial, faça um algoritmo que:

* Receba, inicialmente, o valor mínimo para a indenização;
* Leia um número indeterminado de linhas contendo cada uma os dados de uma casa:
  metragem (m2) e classe (‘A’ ou ‘B’), sendo que a leitura deverá ser encerrada quando o
  usuário digitar a metragem igual a zero.
* Calcule e imprima:
    a. para cada casa, informe o valor a ser pago de indenização ao proprietário,
       considerando que:
        * nas casas de classe ‘A’, acrescenta-se ao valor mínimo inicial R$ 500,00 por metro
        quadrado;
        * nas casas de classe ‘B’, acrescenta-se ao valor mínimo inicial R$ 300,00 por metro
          quadrado.
    b. o valor total gasto pela prefeitura com indenização;
    c. o maior valor pago para indenizar uma casa de classe ‘B’.

Questão 4
Faça um programa ofereça o seguinte menu de opções ao usuário:
* [1] Pode votar?: solicita ao usuário idade e nacionalidade e informe se a pessoa pode votar, sendo
    que podem votar os brasileiros com 16 anos ou mais;
* [2] Ver Categoria: solicita ao usuário a idade de uma pessoa e informe a qual sua categoria,
    considerando a seguinte divisão:
        - Criança - do nascimento aos 11 anos de idade;
        - Adolescente - corresponde à população que possui de 12 a 20 anos de idade;
        - Jovem - corresponde à população que possui de 21 a 30 anos de idade;
        - Adulto – corresponde à população que possui de 31 a 59 anos de idade;
        - Idoso – pessoas com 60 anos de idade ou mais.
* [3] Pode alistar?: solicita o sexo e a idade de uma pessoa e informa se ela deve se alistar no serviço
    militar;
*   Devem se alistar as pessoas do sexo masculino com 18 anos ou mais.
* [4] Encerrar programa: encerra o programa, sendo que o programa deverá ficar solicitando opções ao
    usuário até que ele digite 4.

Importante: Deve ser informado ao usuário quando ele escolher uma opção inválida.


Questão 5
O valor a ser recebido pelos vendedores que participaram de uma feira de vendas de camisetas foi calculado
da seguinte forma: o valor do salário mínimo mais R$ 0.5 por camiseta vendida.
Elabore um programa que:
    * leia, inicialmente, o valor do salário mínimo;
    * leia o nome do vendedor e a quantidade de camisetas vendidas de um número indeterminado de
      vendedores, sendo que a leitura deverá ser encerrada quando o usuário digitar ‘sair’ para o nome do
      vendedor.
    * Calcule e apresente:
        a. para cada vendedor, o nome, a categoria e o valor recebido; A categoria dos operários é
           determinada de acordo com o valor recebido por ele:
            - até 1000: categoria A
            - acima 1000 até 1500: categoria B
            - acima de 1500 até 2000: categoria C
            - acima de 2000: categoria D
        b. o total gasto com pagamento de vendedores;
        c. o nome do vendedor que vendeu a menor quantidade de camisetas, considerando que não
           houve empate.
        * O maior número de camisetas vendidas por um vendedor foi 2512.


Questão 6
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo,
da esquerda para a direita. Em seguida conclua qual dos animais seguintes foi escolhido, através das três
palavras fornecidas.

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima,
com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.
