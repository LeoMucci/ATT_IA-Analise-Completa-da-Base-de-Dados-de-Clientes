import pandas as pd
from scipy import stats

# Carregar a base de clientes
df_clientes = pd.read_csv('https://iafatec.s3.amazonaws.com/atividade/clientes.csv')

# Limpeza de Dados
# Remover registros com idades negativas ou acima de um intervalo plausível (18-70 anos)
df_clientes = df_clientes[(df_clientes['idade'] >= 18) & (df_clientes['idade'] <= 70)]

# Remover registros com alturas fora do intervalo normal (150-200 cm)
df_clientes = df_clientes[(df_clientes['altura_cm'] >= 150) & (df_clientes['altura_cm'] <= 200)]

# Uniformizar valores inconsistentes em 'sexo'
df_clientes['sexo'] = df_clientes['sexo'].replace(['Desconhecido', 'Outro'], 'Não Informado')

# Remover registros com salários fora do intervalo razoável (0-100000)
df_clientes = df_clientes[(df_clientes['salario'] >= 0) & (df_clientes['salario'] <= 100000)]

# Calcular a média para atributos numéricos
media = df_clientes[['idade', 'altura_cm', 'salario', 'peso']].mean()

# Calcular a mediana para atributos numéricos
mediana = df_clientes[['idade', 'altura_cm', 'salario', 'peso']].median()

# Calcular a moda para atributos numéricos
moda_idade = stats.mode(df_clientes['idade'].dropna(), keepdims=True)
moda_altura = stats.mode(df_clientes['altura_cm'].dropna(), keepdims=True)
moda_salario = stats.mode(df_clientes['salario'].dropna(), keepdims=True)
moda_peso = stats.mode(df_clientes['peso'].dropna(), keepdims=True)

moda = {
    'idade': moda_idade.mode[0] if moda_idade.count[0] > 0 else 'Nenhuma moda',
    'altura_cm': moda_altura.mode[0] if moda_altura.count[0] > 0 else 'Nenhuma moda',
    'salario': moda_salario.mode[0] if moda_salario.count[0] > 0 else 'Nenhuma moda',
    'peso': moda_peso.mode[0] if moda_peso.count[0] > 0 else 'Nenhuma moda'
}

# Calcular o intervalo interquartil para atributos numéricos
intervalo_interquartil = df_clientes[['idade', 'altura_cm', 'salario', 'peso']].quantile([0.25, 0.75])
intervalo_interquartil.index = ['Q1', 'Q3']

# Organizar os resultados em um DataFrame
resultados = pd.DataFrame({
    'Média': media,
    'Mediana': mediana,
    'Moda': list(moda.values()),
    'Q1': intervalo_interquartil.loc['Q1'],
    'Q3': intervalo_interquartil.loc['Q3']
})

# Exibir os resultados em forma de tabela
print("\nResumo Estatístico dos Atributos Numéricos:\n")
print(resultados.to_string())

# Descrever a distribuição de frequência dos atributos categóricos
frequencia_sexo = df_clientes['sexo'].value_counts().rename_axis('Sexo').reset_index(name='Frequência')
frequencia_genero_musical = df_clientes['genero_musical_favorito'].value_counts().rename_axis('Gênero Musical Favorito').reset_index(name='Frequência')
frequencia_cidade = df_clientes['cidade'].value_counts().rename_axis('Cidade').reset_index(name='Frequência')
frequencia_profissao = df_clientes['profissao'].value_counts().rename_axis('Profissão').reset_index(name='Frequência')

# Exibir as frequências em forma de tabela
print("\nDistribuição de Frequência dos Atributos Categóricos:\n")
print("Sexo:\n", frequencia_sexo.to_string(index=False))
print("\nGênero Musical Favorito:\n", frequencia_genero_musical.to_string(index=False))
print("\nCidade:\n", frequencia_cidade.to_string(index=False))
print("\nProfissão:\n", frequencia_profissao.to_string(index=False))
