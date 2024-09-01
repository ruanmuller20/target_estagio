#Não encontrei o arquivo Json no Gupy, por isso crei minha própia tabela com valores diários
faturamento_dia = [
    {"dia": 1, "valor": 1500.00},
    {"dia": 2, "valor": 1200.70},
    {"dia": 3, "valor": 2000.134},
    {"dia": 4, "valor": 800.234},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 0.0},
    {"dia": 7, "valor": 4555.00},
    {"dia": 8, "valor": 3534.123},
    {"dia": 9, "valor": 6356.445},
    {"dia": 10, "valor": 5455.998},
    {"dia": 11, "valor": 3500.00},
    {"dia": 12, "valor": 2200.70},
    {"dia": 13, "valor": 200.134},
    {"dia": 14, "valor": 900.234},
    {"dia": 15, "valor": 0.0},
    {"dia": 16, "valor": 0.0},
    {"dia": 17, "valor": 5455.00},
    {"dia": 18, "valor": 5634.123},
    {"dia": 19, "valor": 9656.445},
    {"dia": 20, "valor": 2455.998},
    {"dia": 21, "valor": 3500.00},
    {"dia": 22, "valor": 2400.70},
    {"dia": 23, "valor": 1000.134},
    {"dia": 24, "valor": 500.234},
    {"dia": 25, "valor": 0.0},
    {"dia": 26, "valor": 0.0},
    {"dia": 27, "valor": 3455.00},
    {"dia": 28, "valor": 5534.123},
    {"dia": 29, "valor": 2546.445},
    {"dia": 30, "valor": 3455.998}
]


dados_validos = [dia['valor'] for dia in faturamento_dia if dia ['valor'] > 0]

valor_maximo = max(dados_validos)
valor_minimo = min (dados_validos)

print(f'O maior valor de faturamento ocorrido em um dia do mês {valor_maximo:.2f}R$')
print(f'O menor valor de faturamento ocorrido em um dia do mês {valor_minimo:.2f}R$')

media = sum(dados_validos)/len(dados_validos)
print(f'Média mensal de {media:.2f}R$')

media_acima = len([valor for valor in dados_validos if valor > media])
print(f'Foram {media_acima} dias no mês em que o valor de faturamento diário foi superior à média mensal')
