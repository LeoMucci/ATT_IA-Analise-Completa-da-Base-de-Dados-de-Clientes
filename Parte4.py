import pandas as pd

# Carregar a base de clientes
df_clientes = pd.read_csv('https://iafatec.s3.amazonaws.com/atividade/clientes.csv')

# Integração de Dados
# (Para este exemplo, assumimos que os dados já estão integrados. Em um caso real, descreveríamos
# a necessidade de integrar dados de múltiplas fontes. Por exemplo, combinar dados de diferentes sistemas.)

# Valores Inconsistentes
# Identificar e corrigir valores inconsistentes nos atributos:
# - Idade negativa ou fora do intervalo plausível (18-70 anos)
# - Altura fora do intervalo normal (150-200 cm)
# - Sexo inconsistente

# Corrigir idades inconsistentes
df_clientes = df_clientes[(df_clientes['idade'] >= 18) & (df_clientes['idade'] <= 70)]

# Corrigir alturas inconsistentes
df_clientes = df_clientes[(df_clientes['altura_cm'] >= 150) & (df_clientes['altura_cm'] <= 200)]

# Uniformizar valores inconsistentes em 'sexo'
df_clientes['sexo'] = df_clientes['sexo'].replace(['Desconhecido', 'Outro'], 'Não Informado')

# Corrigir salários inconsistentes (remover valores fora do intervalo razoável)
df_clientes = df_clientes[(df_clientes['salario'] >= 0) & (df_clientes['salario'] <= 100000)]

# Corrigir valores inconsistentes em 'score_bom_pagador'
df_clientes['score_bom_pagador'] = df_clientes['score_bom_pagador'].replace({'A': 10, 'B': 8, 'C': 6, 'D': 4, 'E': 2})

# Redundância de Dados
# Identificar e remover dados redundantes (duplicatas e colunas redundantes)
# Remover duplicatas
df_clientes = df_clientes.drop_duplicates()

# Remover colunas redundantes (exemplo: suponha que a coluna 'idade' seja redundante)
# df_clientes = df_clientes.drop(columns=['idade'])

# Exibir o DataFrame Processado
print("\nDataFrame Processado:\n")
print(df_clientes.head())

print("\nResumo do DataFrame Processado:\n")
print(df_clientes.info())

print("\nEstatísticas Descritivas do DataFrame Processado:\n")
print(df_clientes.describe())
