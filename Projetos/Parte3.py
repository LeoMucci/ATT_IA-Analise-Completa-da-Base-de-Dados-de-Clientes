import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar a base de clientes
df_clientes = pd.read_csv('https://iafatec.s3.amazonaws.com/atividade/clientes.csv')

# Limpeza de Dados
df_clientes = df_clientes[(df_clientes['idade'] >= 18) & (df_clientes['idade'] <= 70)]
df_clientes = df_clientes[(df_clientes['altura_cm'] >= 150) & (df_clientes['altura_cm'] <= 200)]
df_clientes['sexo'] = df_clientes['sexo'].replace(['Desconhecido', 'Outro'], 'Não Informado')
df_clientes = df_clientes[(df_clientes['salario'] >= 0) & (df_clientes['salario'] <= 100000)]

# Análise de Correlação
correlacao = df_clientes[['idade', 'altura_cm', 'salario', 'peso']].corr()

# Identificar pares de atributos com correlação forte
correlacao_forte = correlacao[(correlacao > 0.7) | (correlacao < -0.7)]
print("\nMatriz de Correlação:\n")
print(correlacao.to_string())

print("\nPares de Atributos com Correlação Forte (|corr| > 0.7):\n")
print(correlacao_forte.to_string())

# Representações Gráficas

# Histogramas para atributos numéricos
for coluna in ['idade', 'altura_cm', 'salario', 'peso']:
    plt.figure()
    sns.histplot(df_clientes[coluna], kde=True)
    plt.title(f'Histograma de {coluna}')
    plt.xlabel(coluna)
    plt.ylabel('Frequência')
    plt.savefig(f'histograma_{coluna}.png')

# Box plots para atributos numéricos (individuais)
for coluna in ['idade', 'altura_cm', 'salario', 'peso']:
    plt.figure()
    sns.boxplot(y=df_clientes[coluna])
    plt.title(f'Box Plot de {coluna}')
    plt.ylabel(coluna)
    plt.savefig(f'boxplot_{coluna}.png')

# Gráficos de dispersão para pares de atributos com correlação forte
for coluna1 in ['idade', 'altura_cm', 'salario', 'peso']:
    for coluna2 in ['idade', 'altura_cm', 'salario', 'peso']:
        if coluna1 != coluna2 and abs(correlacao.loc[coluna1, coluna2]) > 0.7:
            plt.figure()
            sns.scatterplot(x=df_clientes[coluna1], y=df_clientes[coluna2])
            plt.title(f'Dispersão entre {coluna1} e {coluna2}')
            plt.xlabel(coluna1)
            plt.ylabel(coluna2)
            plt.savefig(f'dispersao_{coluna1}_{coluna2}.png')

# Mapa de calor para a matriz de correlação
plt.figure(figsize=(10, 8))
sns.heatmap(correlacao, annot=True, cmap='coolwarm', center=0)
plt.title('Mapa de Calor da Matriz de Correlação')
plt.savefig('mapa_calor_correlacao.png')

plt.show()
