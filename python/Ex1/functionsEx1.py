def lucroOrDespesa(qtPass, valorDaPass, despesa):
    if (qtPass * valorDaPass) > despesa:
        return f'Houve lucro!'

    elif (qtPass * valorDaPass) < despesa:
        return f'Houve prejuízo!'

    else:
        return 'A viagem se pagou!'
    
def viagensA(ident, qtA):
    if ident == 'A':
        qtA += 1
        return qtA
    else:
        return qtA

def qtPessoasDia(ident, dataDaViagem, qtPessoasDia23_12_22, qtPass):
    if ident == 'B' and dataDaViagem == '23/12/22':
        qtPessoasDia23_12_22 = qtPessoasDia23_12_22 + qtPass
        return qtPessoasDia23_12_22
    else:
        return qtPessoasDia23_12_22
    
def identMaior(qtPass, qtMaiorTransporte, identMaiorTransporte, ident):
    if qtPass > qtMaiorTransporte:
        qtMaiorTransporte = qtPass
        identMaiorTransporte = ident
        return qtMaiorTransporte, identMaiorTransporte
    else:
        return qtMaiorTransporte, identMaiorTransporte