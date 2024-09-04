import json

with open('dados.json') as arquivo:
  faturamento_dia = json.load(arquivo)


dados_validos = [dia['valor'] for dia in faturamento_dia if dia ['valor'] > 0]

valor_maximo = max(dados_validos)
valor_minimo = min (dados_validos)

print(f'O maior valor de faturamento ocorrido em um dia do mês {valor_maximo:.2f}R$')
print(f'O menor valor de faturamento ocorrido em um dia do mês {valor_minimo:.2f}R$')

media = sum(dados_validos)/len(dados_validos)
print(f'Média mensal de {media:.2f}R$')

media_acima = len([valor for valor in dados_validos if valor > media])
print(f'Foram {media_acima} dias no mês em que o valor de faturamento diário foi superior à média mensal')
