def jurosCompostos(capital, taxa, tempo):
    taxaConvertida = taxa / 100
    montante = capital * (1 + taxaConvertida) ** tempo
    montanteFinal = f'R${montante:_.2f}'
    return print(montanteFinal.replace('.', ',').replace('_', '.'),)

jurosCompostos(42000, 9, 4)

