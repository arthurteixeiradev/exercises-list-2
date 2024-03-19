def podeVotar(idade, nacionalidade):
    if idade >= 16 and nacionalidade == 'brasileiro':
        return f'Pode votar!'
    else:
        return f'Não pode votar!'
    
def categoria(idade):
    if idade <= 11:
        return f'Criança - do nascimento aos 11 anos de idade.'
    elif idade >= 12 and idade <= 20:
        return f'Adolescente - corresponde à população que possui de 12 a 20 anos de idade.'
    elif idade >= 21 and idade <= 30:
        return f'Jovem - corresponde à população que possui de 21 a 30 anos de idade.'
    elif idade >= 31 and idade <= 59:
        return f'Adulto – corresponde à população que possui de 31 a 59 anos de idade.'
    else:
        return f'Idoso – pessoas com 60 anos de idade ou mais.'
    
def alistar(sexo, idade):
    if sexo == 'masculino' and idade >= 18:
        return f'Pode alistar!'
    else:
        return f'Não pode alistar!'
