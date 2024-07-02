# Sprint III
## Data Engineering
### Author : Rafael Puyau
### Date : 2024-06-30

#### Objetivo

O problema em questão reside na intersecção entre a vida moderna atribulada e as demandas incessantes por resultados, culminando em uma atmosfera de pressão constante. Dentro desse contexto, surge a necessidade premente de identificar se os indivíduos estão em risco de sofrer ataques cardíacos devido ao estresse desencadeado por essa turbulência cotidiana.

Além disso, enfrentamos o desafio da sobrecarga informacional, onde somos inundados por um volume avassalador de dados, tornando-se crucial filtrar o que realmente agrega valor em meio a esse mar de informações.

A preocupação com a saúde, incluindo hábitos alimentares e atividade física regular, muitas vezes é deixada em segundo plano diante das exigências do mundo moderno. Essa negligência pode resultar em consequências graves para a saúde a longo prazo.

No entanto, à medida que avançamos, a tecnologia, especialmente o machine learning, emerge como uma ferramenta vital para nos auxiliar na busca por um equilíbrio saudável. Ela oferece a capacidade de analisar dados complexos, prever e extrair insights significativos, auxiliando os seres humanos na gestão do estresse, na adoção de hábitos saudáveis e na prevenção de doenças cardiovasculares.

Assim, a descrição do problema abrange não apenas os desafios enfrentados na vida moderna, mas também as oportunidades oferecidas pela tecnologia para mitigar esses desafios e promover um estilo de vida mais equilibrado e saudável.

#### Detalhamento
##### Busca pelos dados
O conjunto de dados **heart** foi, inicialmente, obtido no kaggle, uma fonte reconhecida por disponibilizar conjuntos de dados de alta qualidade para projetos de machine learning, data science e data engineering. Isso garante a confiabilidade e a integridade dos dados utilizados nesta sprint.

##### Coleta 
Para este trabalho, em específico, e para demonstrar um processo, mínimo de ETL, optei por usar o dataset que já se encontra neste repositório, fazendo a carga do mesmo através da `raw url` que o Github disponibiliza.

##### Carga
A ingestão na nuvem do **Databricks** foi realizada através do comandos abaixo: 

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
Chegou o momento de se solucionar o problema em questão, definido preliminarmente nos objetivos. Deve-se buscar respostas para as perguntas elencadas. Para cada resposta obtida tecnicamente através da análise dos dados deve haver uma discussão do seu resultado, conectando os números obtidos às respostas ao problema a ser solucionado.

Ao final, deve haver uma discussão de uma forma geral sobre a solução do problema a partir das discussões de cada resposta.

Aqui, podem ser utilizadas bibliotecas Python vistas na disciplina Análise Exploratória e Pré-Processamento de Dados, ou as ferramentas vistas na disciplina Visualização de Informação. Entretanto, caso não tenha ainda cursado estas disciplinas, é possível responder as perguntas do objetivo somente através da linguagem SQL, objeto da disciplina de Banco de Dados ou através da linguagem de consulta do banco NoSQL escolhido, objeto da disciplina de Data Warehouse.

