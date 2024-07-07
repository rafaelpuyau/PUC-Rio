# Sprint III
## Data Engineering
### Author : Rafael Puyau
### Date : 2024-07-12

#### Objetivo do MVP 

Construir um pipeline de dados utilizando tecnologias na nuvem. Neste pipeline será necessário a busca, coleta, modelagem, carga e análise de dados.

#### Objetivo

O problema em questão reside na intersecção entre a vida moderna atribulada e as demandas incessantes por resultados, culminando em uma atmosfera de pressão constante. Dentro desse contexto, surge a necessidade premente de identificar se os indivíduos estão em risco de sofrer ataques cardíacos devido ao estresse desencadeado por essa turbulência cotidiana.

Além disso, enfrentamos o desafio da sobrecarga informacional, onde somos inundados por um volume avassalador de dados, tornando-se crucial filtrar o que realmente agrega valor em meio a esse mar de informações.

A preocupação com a saúde, incluindo hábitos alimentares e atividade física regular, muitas vezes é deixada em segundo plano diante das exigências do mundo moderno. Essa negligência pode resultar em consequências graves para a saúde a longo prazo.

No entanto, à medida que avançamos, a tecnologia, especialmente o machine learning, emerge como uma ferramenta vital para nos auxiliar na busca por um equilíbrio saudável. Ela oferece a capacidade de analisar dados complexos, prever e extrair insights significativos, auxiliando os seres humanos na gestão do estresse, na adoção de hábitos saudáveis e na prevenção de doenças cardiovasculares.

A engenharia de dados desempenha um papel crucial na viabilização de dados e modelos de machine learning. Isso se dá por diversos fatores como:

1. Coleta e ingestão de dados
   * Aquisição de dados em tempo real
   * Tratamento e pré-processamento
   * Ingestão de alta velocidade
2. Infraestrutura e Arquitetura
   * Arquitetura escalável
   * Monitoramento e otimização
   * Segurança e governança
3. Modelos de machine learning
   * Preparação de dados para ML
   * Implementação e treinamento de modelos
   * Monitoramento e retreinamento
4. Disponibilização de dados e modelos
   * APIs e interfaces
   * Visualização e comunicação
   * Integração com sistemas
  
Desta forma, a etapa da engenharia de dados é essencial para construir a infraestrutura e os processos necessários para disponibilizar dados e modelos de ML relevantes em tempo real, permitindo que as organizações tomem decisões mais rápidas, inteligentes e baseadas em dados.

Assim, a descrição do problema abrange não apenas os desafios enfrentados na vida moderna, mas também as oportunidades oferecidas pela tecnologia para mitigar esses desafios e promover um estilo de vida mais equilibrado e saudável.

**Perguntas**

* Qual a distribuição entre pessoas do sexo masculino e feminino?
* Qual a quantidade entre pessoas do sexo masculino e feminino de apresentarem tendência de ataque do coração?
* Qual a quantidade da tendência de ataque do coração por tipo de dor no peito?
* Qual a quantidade de pessoas do sexo masculino e feminino por nível de talassemia?
* Qual a quantidade da tendência de ataque do coração por slope?
* Quantas pessoas do sexo masculino e do sexo feminino tem entre 30 e 50 anos?
* Quantas pessoas, por sexo, abaixo dos 50 anos possem tendência de um ataque do coração?
* Qual a média de idade das mulheres entrevistadas que não possuem tendência de sofrer de um ataque do coração?
* Qual a idade da pessoa mais nova e mais velha do conjunto de dados, por sexo?
* Quantas pessoas, por faixa etária, com colesterol acima de 300 apresentam tendência de um ataque do coração?

#### Plataforma

A plataforma utilizada foi o **Databricks Community Edition**.

#### Detalhamento
##### Busca pelos dados
O conjunto de dados **hearts** foi, inicialmente, obtido no [kaggle](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset), uma fonte reconhecida por disponibilizar conjuntos de dados de alta qualidade para projetos de machine learning, data science e data engineering. Isso garante a confiabilidade e a integridade dos dados utilizados nesta sprint.

##### Coleta 
Para este trabalho, em específico, e para demonstrar um processo, mínimo de ETL, optei por usar o dataset que já se encontra neste repositório - [hearts.csv](https://raw.githubusercontent.com/rafaelpuyau/PUC-Rio/main/hearts.csv), fazendo a carga do mesmo através da `raw url` que o Github disponibiliza, salvando-o no _databricks file system_ em formato `parquet`. Após esta etapa, foi criada uma tabela temporária para a execução dos comandos `SQL` para responder as perguntas.

##### Modelagem

Trata-se de um arquivo flat em formato CSV desnormalizado para facilitar a análise de dados e a criação de modelos de machine learning. De fato, essa abordagem oferece diversos benefícios que otimizam o processo de ETL (Extração, Transformação e Carga) e a análise de dados, especialmente em grandes conjuntos de dados. 

A simplificação do processo de ETL com a redução de junções complexas como `JOINS` entre tabelas reduz significamente o tempo de processamento. Uma maior eficiência é obtida devido a estrutura plana do conjunto de dados, permitindo que ferramentas de análise de dados processem os dados de forma mais eficiente, otimizando o tempo de resposta e a performance em geral. 

Vale destacar ainda a redução de custos devido a uma menor infraestutura e a otimização dos recursos computacionais.

* [Clique aqui](https://github.com/rafaelpuyau/PUC-Rio/blob/main/Sprint_III/catalogo_dados.md#dataset-heartscsv) para acessar o **Catálogo de Dados**

##### Carga
A ingestão na nuvem do **Databricks** foi realizada através dos comandos abaixo: 

1. Extração da base de dados que se encontra neste repositório através da `raw _url`
![image](https://github.com/rafaelpuyau/PUC-Rio/assets/67115933/aa567fc1-96a5-4231-96cc-24457e195f85)

2. Conversão para o format `parquet`e salvamento no _databricks file system_
![image](https://github.com/rafaelpuyau/PUC-Rio/assets/67115933/b6ed4403-aa70-4ac6-8578-5bed208e4641)

3. Criação da tabela temporária para usar os comandos `SQL`
![image](https://github.com/rafaelpuyau/PUC-Rio/assets/67115933/206c7c69-2517-43b0-b6a2-ee0c641a97cf)

##### Análise
###### Qualidade de dados
O tratamento da qualidade dos dados foi realizado na camada `silver` e encontra-se na wiki todas as etapas e ações realizadas. [Clique aqui](https://github.com/rafaelpuyau/PUC-Rio/wiki/Documenta%C3%A7%C3%A3o-%E2%80%90-Fase-II) para conferir.

###### Solução do problema
Todas as 10 perguntas foram respondidas na camada `silver` através de comandos `SQL`e em `PySpark` e na camada `gold` foram gerados gráficos para melhor visualização. Acesse a seção **Wiki** para conferir os resultados. 
