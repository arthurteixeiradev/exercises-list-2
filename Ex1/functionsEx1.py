def lucroOrDespesa(qtPass, valorDaPass, despesa):
    if (qtPass * valorDaPass) > despesa:
        return f'Houve lucro!'

    elif (qtPass * valorDaPass) < despesa:
        return f'Houve prejuízo!'

    else:
        return 'A viagem se pagou!'