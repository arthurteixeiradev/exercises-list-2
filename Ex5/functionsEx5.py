def calcular(nome, salario, qtCamiseta):
    
    if qtCamiseta <= 1000:
        categoria = 'A'
        valorRecebido = (qtCamiseta * 0.5) + salario
    elif qtCamiseta <= 1500:
        categoria = 'B'
        valorRecebido = (qtCamiseta * 0.5) + salario
    elif qtCamiseta <= 2000:
        categoria = 'C'
        valorRecebido = (qtCamiseta * 0.5) + salario
    else:
        categoria = 'D'
        valorRecebido = (qtCamiseta * 0.5) + salario

    return f'{"-"*60}\nVendedor: {nome}\nCategoria: {categoria}\nSalário: R${valorRecebido}\n{"-"*60}'

def totalGasto(qtCamiseta, salario):
    totalGastoV = (qtCamiseta * 0.5) + salario
    return totalGastoV

