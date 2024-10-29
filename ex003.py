import json
import pandas as pd

#carrega os dados do arquivo Json
with open('dados.json', 'r') as file:
    dados = json.load(file)

#converte os dados para um DataFrame do pandas
df = pd.DataFrame(dados)

#filtra so os dias com faturamento maior que zero
faturamentos = df[df["valor"] > 0]["valor"]

#calcula o menor e o maior valor do faturamento
menor_faturamento = faturamentos.min()
maior_faturamento = faturamentos.max()

#calcula a media mensal de faturamento, tirando os dias sem faturamento
media_mensal = faturamentos.mean()

#conta o numero de dias em que o faturamento foi superior à media mensal
dias_acima_media = (faturamentos > media_mensal).sum()

# Exibe os dados em uma tabela
print("Tabela de Faturamento Diário:")
print(df)

# Exibe os resultados finais
print(f"\nMenor valor de faturamento em um dia do mês: {menor_faturamento:.2f}")
print(f"Maior valor de faturamento em um dia do mês: {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
print(f"Para posteriores conferências aqui está a média mensal: {media_mensal:.4f}")