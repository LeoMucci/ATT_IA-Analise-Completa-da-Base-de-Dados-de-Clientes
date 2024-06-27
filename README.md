# 📊 Relatório Completo de Análise e Transformação de Dados

### 🎯 Objetivo:
O objetivo deste projeto foi aplicar conceitos de estatística descritiva, medidas de dispersão, análise de correlação, integração de dados, correção de valores inconsistentes, remoção de redundâncias e transformação de dados em uma base de clientes. Este relatório documenta detalhadamente todas as etapas realizadas, os métodos utilizados e os resultados obtidos.

---

## Parte 1: Estatística Descritiva

### 1.1 Carregamento e Limpeza dos Dados

#### 📚 Bibliotecas Utilizadas:
- pandas: Para manipulação e análise de dados.
- scipy: Para cálculo da moda.

#### 🔧 Funções e Métodos:
- `pd.read_csv()`: Carrega a base de dados de um arquivo CSV.
- `DataFrame.drop_duplicates()`: Remove registros duplicados.
- `DataFrame.replace()`: Substitui valores inconsistentes.
- `DataFrame.quantile()`: Calcula os quartis dos dados.

#### 💻 Código:
```python
import pandas as pd
from scipy import stats

# Carregar a base de clientes
df_clientes = pd.read_csv('https://iafatec.s3.amazonaws.com/atividade/clientes.csv')

# Limpeza de Dados
df_clientes = df_clientes[(df_clientes['idade'] >= 18) & (df_clientes['idade'] <= 70)]
df_clientes = df_clientes[(df_clientes['altura_cm'] >= 150) & (df_clientes['altura_cm'] <= 200)]
df_clientes['sexo'] = df_clientes['sexo'].replace(['Desconhecido', 'Outro'], 'Não Informado')
df_clientes = df_clientes[(df_clientes['salario'] >= 0) & (df_clientes['salario'] <= 100000)]
df_clientes['score_bom_pagador'] = df_clientes['score_bom_pagador'].replace({'A': 10, 'B': 8, 'C': 6, 'D': 4, 'E': 2})
df_clientes = df_clientes.drop_duplicates()
```

#### 📄 Descrição:
- **Carregamento dos Dados**: Utilizamos a função `pd.read_csv()` para carregar a base de clientes de um arquivo CSV.
- **Limpeza dos Dados**: Removemos registros com idades, alturas, sexos e salários inconsistentes, além de registros duplicados.

### 1.2 Cálculo das Estatísticas Descritivas

#### 🔧 Funções e Métodos:
- `DataFrame.mean()`: Calcula a média dos dados.
- `DataFrame.median()`: Calcula a mediana dos dados.
- `stats.mode()`: Calcula a moda dos dados.
- `DataFrame.quantile()`: Calcula os quartis dos dados.

#### 💻 Código:
```python



```

#### 📄 Descrição:
- **Cálculo da Média, Mediana, Moda e Intervalo Interquartil**: Utilizamos métodos do Pandas e SciPy para calcular as estatísticas descritivas dos atributos numéricos.

### 1.3 Distribuição de Frequência dos Atributos Categóricos

#### 🔧 Funções e Métodos:
- `DataFrame.value_counts()`: Conta a frequência dos valores categóricos.
- `Series.rename_axis()`: Renomeia o eixo de uma Series.
- `Series.reset_index()`: Reseta o índice da Series.

#### 💻 Código:
```python



```

#### 📄 Descrição:
- **Distribuição de Frequência**: Utilizamos `value_counts()` para contar a frequência dos valores categóricos e formatamos a saída com `rename_axis()` e `reset_index()`.

---

## Parte 2: Medidas de Dispersão, Variância e Desvio-Padrão

### 2.1 Carregamento e Limpeza dos Dados
Os dados foram carregados e limpos conforme descrito na Parte 1.

### 2.2 Cálculo das Medidas de Dispersão

#### 🔧 Funções e Métodos:
- `DataFrame.max()`: Calcula o valor máximo dos dados.
- `DataFrame.min()`: Calcula o valor mínimo dos dados.
- `DataFrame.var()`: Calcula a variância dos dados.
- `DataFrame.std()`: Calcula o desvio-padrão dos dados.

#### 💻 Código:
```python



```

#### 📄 Descrição:
- **Cálculo da Amplitude, Variância e Desvio-Padrão**: Utilizamos métodos do Pandas para calcular as medidas de dispersão dos atributos numéricos.

---

## Parte 3: Análise de Correlação e Representações Gráficas

### 3.1 Carregamento e Limpeza dos Dados
Os dados foram carregados e limpos conforme descrito na Parte 1.

### 3.2 Análise de Correlação

#### 🔧 Funções e Métodos:
- `DataFrame.corr()`: Calcula a matriz de correlação dos dados.

#### 💻 Código:
```python



```

#### 📄 Descrição:
- **Análise de Correlação**: Utilizamos o método `corr()` do Pandas para calcular a matriz de correlação entre os atributos numéricos.

### 3.3 Representações Gráficas

#### 📚 Bibliotecas Utilizadas:
- matplotlib: Para geração de gráficos.
- seaborn: Para visualização de dados estatísticos.

#### 🔧 Funções e Métodos:
- `sns.histplot()`: Gera histogramas.
- `sns.boxplot()`: Gera box plots.
- `sns.scatterplot()`: Gera gráficos de dispersão.
- `sns.heatmap()`: Gera mapas de calor.

#### 💻 Código:
```python



```

#### 📄 Descrição:
- **Histogramas, Box Plots, Gráficos de Dispersão e Mapas de Calor**: Utilizamos seaborn e matplotlib para criar diversas visualizações gráficas, que ajudam na interpretação dos dados.

---

## Parte 4: Integração de Dados, Valores Inconsistentes e Redundância de Dados

### 4.1 Integração de Dados

#### 📄 Descrição:
Assumimos que os dados já estão integrados. Em um cenário real, descreveríamos a necessidade de integrar dados de múltiplas fontes, como combinar dados de diferentes sistemas ou departamentos.

### 4.2 Identificação e Correção de Valores Inconsistentes

#### 🔧 Funções e Métodos:
- `DataFrame.replace()`: Substitui valores inconsistentes.
- `DataFrame.drop_duplicates()`: Remove registros duplicados.

#### 💻 Código:
```python



```

#### 📄 Descrição:
- **Correção de Valores Inconsistentes**: Removemos registros com valores inconsistentes em atributos como idade, altura, sexo, salário e score bom pagador.

### 4.3 Identificação e Remoção de Redundâncias

#### 🔧 Funções e Métodos:
- `DataFrame.drop_duplicates()`: Remove registros duplicados.
- `DataFrame.drop()`: Remove colunas redundantes.

#### 💻 Código:
```python



```

#### 📄 Descrição:
- **Remoção de Redundâncias**: Removemos registros duplicados e colunas redundantes, garantindo a consistência dos dados.

---

## Parte 5: Transformação de Dados

### 5.1 Normalização de Dados

#### 📚 Bibliotecas Utilizadas:
- sklearn.preprocessing: Para normalização e codificação dos dados.

#### 🔧 Funções e Métodos:
- `MinMaxScaler()`: Aplica a normalização Min-Max nos dados.

#### 💻 Código:
```python



```

#### 📄 Descrição:
- **Normalização de Dados**: Utilizamos `MinMaxScaler` para normalizar os atributos numéricos no intervalo [0, 1].

### 5.2 Codificação de Dados Categóricos

#### 🔧 Funções e Métodos:
- `OneHotEncoder()`: Aplica a codificação One-Hot nos dados categóricos.

#### 💻 Código:
```python



```

#### 📄 Descrição:
- **Codificação de Dados Categóricos**: Utilizamos `OneHotEncoder` para transformar atributos categóricos em variáveis dummy, permitindo seu uso em modelos de aprendizado de máquina.
