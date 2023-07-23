# -*- coding: utf-8 -*-
"""Sprint II.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14NqWVOnfcCIwUSEP60fnU7z6vcEajlhh

# MVP Sprint II

## Definição do problema

__Objetivo__ : entender e descrever claramente o problema que está sendo resolvido

* Qual é a descrição do problema?
* Você tem premissas ou hipóteses sobre o problema? Quais?
* Que restrições ou condições foram impostas para selecionar os dados?
*
"""

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import (
    train_test_split,
    cross_val_score
)
from sklearn.linear_model import (
    LinearRegression,
    Lasso
)
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import r2_score
import warnings

# Configurações
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.max_columns', None)

warnings.filterwarnings('ignore')

dataset_part1 = r'https://raw.githubusercontent.com/rafaelpuyau/PUC-Rio/main/fipe_cars_part1.csv'
dataset_part2 = r'https://raw.githubusercontent.com/rafaelpuyau/PUC-Rio/main/fipe_cars_part2.csv'
dataset_part3 = r'https://raw.githubusercontent.com/rafaelpuyau/PUC-Rio/main/fipe_cars_part3.csv'
dataset_part4 = r'https://raw.githubusercontent.com/rafaelpuyau/PUC-Rio/main/fipe_cars_part4.csv'

df = pd.DataFrame()

for i in range(1, 5):
  df_aux = pd.read_csv(globals()[f'dataset_part{i}'])
  df = pd.concat([df, df_aux])

# df = df.sample(frac=.05)

print(df.shape)

"""* __year_of_reference__: year of reference of the observation, i.e., the year the data corresponds to.

* __moth_of_reference__: month of reference of the observation, i.e., the month the data corresponds to. The average price is calculated by FIPE each month.

* __fipe_code__: unique id corresponding to a model for easy search on FIPE webpage.

* __authentication__: unique code that authenticates the consult in FIPE's site.
brand: car's make.

* __model__: a description of the car containing the name and other descriptive information, as provided in FIPE table.

* __fuel__: fuel used by the car. Some of gas cars are actually alcohol and gas (totalflex), which is common in Brazil.

* __gear__: the way gears are shifted.

* __engine_size__: Engine size measured in cubic centimeters.

* __year_model__: those values corresponds to the year of reference, and may not be the same of the year of manufacture, which in case will corresponds to a year before year_model. Observations with year_model = year_of_reference mean the car is brand new for that year of reference, i.e., a 2021 car with year_of_reference = 2021 and moth_of_reference = July mean that the observation (mainly the average price) corresponds to a brand new car in the year of 2021, of the month of July. The same model may have a different average price for different month.

* __avg_price_brl__: average car's price, as measured by FIPE, in BRL
"""

print(df.head())

print(df.shape)

print(df.info())

print(df.isna().sum())

# Distribuição das variáveis categóricas
for col in ['month_of_reference', 'brand', 'fuel', 'gear', 'year_model']:
  print(df[col].value_counts())
  print('---' * 20)

"""Uma breve e simples __EDA__ (Exploratory Data Analysis) para verificar possíveis correlações e entender melhor a base"""

print(df.describe())

# Possível tratamento de outliers
print(df['avg_price_brl'].describe(percentiles=[.9]))

print(df['avg_price_brl'].describe(percentiles=[.9])['90%'].round(2))

avg_price_brl_90 = df['avg_price_brl'].describe(percentiles=[.9])['90%'].round(2)
print(df.loc[df['avg_price_brl'] < avg_price_brl_90, :].describe())

# sns.distplot(df.loc[df['avg_price_brl'] < avg_price_brl_90, 'avg_price_brl'])

# sns.pairplot(df.loc[df['avg_price_brl'] < avg_price_brl_90].sample(500))

"""## Separando variáveis preditoras e target"""

print(df.columns)

print(df['brand'].nunique())

# As colunas fipe_code, authentication, brand e model serão removidas pois não ajudarão no modelo

X = df.drop(['fipe_code', 'authentication', 'brand', 'model', 'avg_price_brl'], axis='columns')
y = df['avg_price_brl']

# Visualizando o X
print(X)

# Visualizando o y
print(y)

"""Fazendo o split (antes do scaling, imputação, codificação das variáveis categóricas)"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=42)

"""**Codificar as variáveis categóricas**

Os algoritmos entendem apenas números! Assim, devemos converter as variáveis categóricas de alguma forma. Para isso, utilizarei o _OneHotEncoding_, uma forma simples de transformar categorias não ordinais em números
"""

# Buscando as colunas que não são numéricas
colunas_categoricas = X_train.select_dtypes(include=[object]).columns
print(colunas_categoricas)

# Criando o objeto que vai transformar as colunas categóricas em diversas colunas numéricas
ohe = OneHotEncoder(sparse=False, drop='first')

print(X_train.shape)

print(X_train['fuel'])

print(ohe.fit_transform(X_train[['fuel']]))

print(ohe.categories_)

# Transformando as variáveis categóricas em numéricas

for col_cat in colunas_categoricas:
  colunas_ohe = ohe.fit_transform(X_train[[col_cat]])
  colunas_ohe_teste = ohe.transform(X_test[[col_cat]])

  categorias_ohe = ohe.categories_[0][1:]

  for indice, nome_categoria in enumerate(categorias_ohe):
    df_categorias = pd.DataFrame(data=colunas_ohe[:, indice], columns=[nome_categoria])
    df_categorias_teste = pd.DataFrame(data=colunas_ohe_teste[:, indice], columns=[nome_categoria])

    X_train[nome_categoria] = colunas_ohe[:, indice]
    X_test[nome_categoria] = colunas_ohe_teste[:, indice]

  X_train = X_train.drop(col_cat, axis='columns')
  X_test = X_test.drop(col_cat, axis='columns')

print(X_train.head())

print(X_test.head())

"""### Treinando os modelos!

#### Regressão Linear
"""

# Criando o objeto de regressão linear
mdl_regressao_linear = LinearRegression()

mdl_regressao_linear.fit(X_train, y_train)

"""Validação do modelo com o Cross Validation"""

# Validação cruzada com r2 (quanto mais próximo de 1, melhor pois as variáveis preditoras explicam a variável target)
scores_regressao_linear = cross_val_score(mdl_regressao_linear, X_train, y_train, scoring='r2', cv=5)
print(scores_regressao_linear)

print(scores_regressao_linear.mean())

"""#### Random Forest"""

# Criando o objeto de random forest
mdl_random_forest = RandomForestClassifier(random_state=42)

mdl_random_forest.fit(X_train, y_train)

# R Quadrado
scores_rf = cross_val_score(mdl_random_forest, X_train, y_train, scoring='r2', cv=5)
print(scores_rf)

print(scores_rf.mean())

"""## Predições com o modelo campeão"""

# Predições na base de teste
predicoes = mdl_random_forest.predict(X_test)

error_score = r2_score(y_test, predicoes)
print(f'R² error: {error_score}')