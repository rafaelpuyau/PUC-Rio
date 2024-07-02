# Catálogo de Dados 
## Dataset: hearts.csv

| Coluna | Descrição |
|:---|:---|
|age |idade em anos com valores entre 29 e 77 anos |
|sex |sexo do paciente, sendo 0 para feminino e 1 para masculino |
|cp | tipo de dor no peito |
|trestbps |pressão arteriaal em repouso |
|chol |colesterol sérico em mg/dl |
|fbs |glicemia em jejum > 120 mg/dl |
|restecg |resultdos eletrocardiográficos em repouso |
|thalach |frequência cardíaca máxima alcançada |
|exang |angina induzida por exercício |
|oldpeak |depressão do segmento ST induzida por exercício em relação ao repouso |
|slope |a inclinação do pico do segmento ST do exercício |
|ca |número de vasos principais coloridos por fluorosopia |
|thal |uma doença sanguínea chamada talassemia |

## Descrição detalhada

O infarto do miocárdio, ou ataque cardíaco, é a morte das células de uma região do músculo do coração por conta da formação de um coágulo que interrompe o fluxo sanguíneo de forma súbita e intensa.

Este dataset possui informações relevantes sobre os pacientes que deram entrada no hospital com este problema.

Atributos : São 14 atributos no total, sendo um deles o target

* age: age in years (idade em anos)
    * valores: entre 29 e 77 anos
* sex:
    * 0 = female
    * 1 = male
* cp: tipo de dor no peito (chest pain type (4 values)):
    * 0 = asymptomatic
    * 1 = atypical angina
    * 2 = non-anginal pain
    * 3 = typical angina
* trestbps: pressão arterial em repouso (em mm Hg na admissão ao hospital) (resting blood pressure (in mm Hg on admission to the hospital))
    * valores: entre 94 e 200
* chol: colesterol sérico em mg/dl (serum cholestoral in mg/dl)
    * valores: entre 126 e 564
* fbs: glicemia em jejum > 120 mg/dl (fasting blood sugar > 120 mg/dl)
    * 0 = false
    * 1 = true
* restecg: resultados eletrocardiográficos em repouso (resting electrocardiographic results):
    * 0 = showing probable or definite left ventricular hypertrophy by Estes’ criteria
    * 1 = normal
    * 2 = having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
* thalach: frequência cardíaca máxima alcançada (maximum heart rate achieved)
    * valores: entre 71 e 202
* exang: angina induzida por exercício (exercise induced angina)
    * 0 = no
    * 1 = yes
* oldpeak: depressão do segmento ST induzida por exercício em relação ao repouso (ST depression induced by exercise relative to rest)
    * valores: entre 0 e 6.2
* slope: a inclinação do pico do segmento ST do exercício (the slope of the peak exercise ST segment)
    * 0 = downsloping
    * 1 = flat
    * 2 = upsloping
* ca: número de vasos principais coloridos por fluorosopia (number of major vessels colored by flourosopy)
    * 0
    * 1
    * 2
    * 3
    * 4
* thal:
   * 0 = no info
   * 1 = fixed defect (no blood flow in some part of the heart)
   * 2 = normal blood flow
   * 3 = reversable defect (a blood flow is observed but it is not normal)
* target:
   * 0 = no
   * 1 = yes

**OBS**: Os nomes e números de segurança social dos pacientes foram recentemente removidos do banco de dados e substituídos por valores fictícios.
