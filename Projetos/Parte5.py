import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

# Carregar a base de clientes
df_clientes = pd.read_csv('https://iafatec.s3.amazonaws.com/atividade/clientes.csv')

# Limpeza de Dados
df_clientes = df_clientes[(df_clientes['idade'] >= 18) & (df_clientes['idade'] <= 70)]
df_clientes = df_clientes[(df_clientes['altura_cm'] >= 150) & (df_clientes['altura_cm'] <= 200)]
df_clientes['sexo'] = df_clientes['sexo'].replace(['Desconhecido', 'Outro'], 'Não Informado')
df_clientes = df_clientes[(df_clientes['salario'] >= 0) & (df_clientes['salario'] <= 100000)]
df_clientes['score_bom_pagador'] = df_clientes['score_bom_pagador'].replace({'A': 10, 'B': 8, 'C': 6, 'D': 4, 'E': 2})

# Remover duplicatas
df_clientes = df_clientes.drop_duplicates()

# Transformação de Dados

# Normalização de Dados
# Selecionando as colunas numéricas para normalização
colunas_numericas = ['idade', 'altura_cm', 'score_bom_pagador', 'salario', 'peso']

# Instanciando o MinMaxScaler
scaler = MinMaxScaler()

# Aplicando a normalização Min-Max
df_clientes[colunas_numericas] = scaler.fit_transform(df_clientes[colunas_numericas])

# Codificação de Dados Categóricos
# Instanciando o OneHotEncoder
encoder = OneHotEncoder(sparse_output=False)

# Codificando o atributo 'sexo'
sexo_encoded = encoder.fit_transform(df_clientes[['sexo']])
sexo_encoded_df = pd.DataFrame(sexo_encoded, columns=encoder.get_feature_names_out(['sexo']))

# Codificando o atributo 'genero_musical_favorito'
genero_encoded = encoder.fit_transform(df_clientes[['genero_musical_favorito']])
genero_encoded_df = pd.DataFrame(genero_encoded, columns=encoder.get_feature_names_out(['genero_musical_favorito']))

# Concatenando as colunas codificadas ao DataFrame original
df_clientes = pd.concat([df_clientes, sexo_encoded_df, genero_encoded_df], axis=1)

# Removendo as colunas originais categóricas
df_clientes = df_clientes.drop(columns=['sexo', 'genero_musical_favorito'])

# Exibir o DataFrame Processado
print("\nDataFrame Processado:\n")
print(df_clientes.head())

print("\nResumo do DataFrame Processado:\n")
print(df_clientes.info())

print("\nEstatísticas Descritivas do DataFrame Processado:\n")
print(df_clientes.describe())
