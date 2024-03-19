def calcular(nome, salario, qtCamiseta):
    
    if qtCamiseta <= 1000:
        categoria = 'A'
        valorRecebido = totalSalario(qtCamiseta, salario)
    elif qtCamiseta <= 1500:
        categoria = 'B'
        valorRecebido = totalSalario(qtCamiseta, salario)
    elif qtCamiseta <= 2000:
        categoria = 'C'
        valorRecebido = totalSalario(qtCamiseta, salario)
    else:
        categoria = 'D'
        valorRecebido = totalSalario(qtCamiseta, salario)

    return f'{"-"*60}\nVendedor: {nome}\nCategoria: {categoria}\nSalário: R${valorRecebido}\n{"-"*60}'

def totalSalario(qtCamiseta, salario):
    totalSalarioPago = (qtCamiseta * 0.5) + salario
    return totalSalarioPago

def menorVender(qtCamiseta, menorQt, menorVendedor, nome):
    if qtCamiseta < menorQt:
        menorQt = qtCamiseta
        menorVendedor = nome
        return menorVendedor, menorQt
    else:
        return menorVendedor, menorQt
    
def maiorQtVendida(qtCamiseta, maiorQt):
    if qtCamiseta > maiorQt:
        maiorQt = qtCamiseta
        return maiorQt
    else:
        return maiorQt