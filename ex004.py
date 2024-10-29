#dicionario com os dados de faturamento por estado
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

#calcula o faturamento total
faturamento_total = sum(faturamento.values())

#calcula e mostra o percentual de representacao de cada estado dentro do valor total mensal da distribuidora
print("Percentual de representação de cada estado no faturamento total:")
for estado, valor in faturamento.items(): #iteração com laço for
    percentual = (valor / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}%")