import pandas as pd

# Carregar a base de clientes
df_clientes = pd.read_csv('https://iafatec.s3.amazonaws.com/atividade/clientes.csv')

# Limpeza de Dados
df_clientes = df_clientes[(df_clientes['idade'] >= 18) & (df_clientes['idade'] <= 70)]
df_clientes = df_clientes[(df_clientes['altura_cm'] >= 150) & (df_clientes['altura_cm'] <= 200)]
df_clientes['sexo'] = df_clientes['sexo'].replace(['Desconhecido', 'Outro'], 'Não Informado')
df_clientes = df_clientes[(df_clientes['salario'] >= 0) & (df_clientes['salario'] <= 100000)]

# Calcular a amplitude para atributos numéricos
amplitude = df_clientes[['idade', 'altura_cm', 'salario', 'peso']].max() - df_clientes[['idade', 'altura_cm', 'salario', 'peso']].min()

# Calcular a variância para atributos numéricos
variancia = df_clientes[['idade', 'altura_cm', 'salario', 'peso']].var()

# Calcular o desvio-padrão para atributos numéricos
desvio_padrao = df_clientes[['idade', 'altura_cm', 'salario', 'peso']].std()

# Organizar os resultados em um DataFrame
resultados_dispersao = pd.DataFrame({
    'Amplitude': amplitude,
    'Variância': variancia,
    'Desvio-Padrão': desvio_padrao
})

# Exibir os resultados em forma de tabela
print("\nMedidas de Dispersão dos Atributos Numéricos:\n")
print(resultados_dispersao.to_string())
