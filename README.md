# 📊 Relatório Completo de Análise e Transformação de Dados

## 📝 Projeto: Análise Completa da Base de Dados de Clientes

### 🎯 Objetivo:
O objetivo deste projeto foi aplicar conceitos de estatística descritiva, medidas de dispersão, análise de correlação, integração de dados, correção de valores inconsistentes, remoção de redundâncias e transformação de dados em uma base de clientes. Este relatório documenta detalhadamente todas as etapas realizadas, os métodos utilizados e os resultados obtidos.

---

## Parte 1: Estatística Descritiva

### 1.1 Carregamento e Limpeza dos Dados

#### 📚 Bibliotecas Utilizadas:
- `pandas`: Para manipulação e análise de dados.
- `scipy`: Para cálculo da moda.

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

