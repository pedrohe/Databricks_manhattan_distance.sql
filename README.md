# 🌎 Cálculo de Distâncias entre Cidades (Databricks / PySpark)

Este repositório contém um projeto desenvolvido no **Databricks Free Edition**, utilizando **PySpark** e **SQL**, para calcular a distância entre cidades a partir de suas coordenadas geográficas (latitude e longitude).  

O objetivo é gerar uma **matriz de distâncias** (em formato tabelar), onde:
- Cada **linha** representa a cidade de origem (`city_a`);
- Cada **coluna** representa a cidade de destino (`city_b`);
- Cada **célula** contém a **distância de Manhattan** entre as duas cidades;
- A diagonal principal é sempre **zero** (distância de uma cidade para ela mesma).

---

## 📂 Estrutura do Projeto

- **`Station`** → Tabela com os dados das cidades (ID, nome, estado, latitude e longitude).
- **Códigos PySpark** → Responsáveis por:
  - Criar a tabela com os dados simulados (`saveAsTable`).
  - Calcular as distâncias entre todas as combinações de cidades.
  - Gerar a matriz de distâncias de forma automática (usando `groupBy` + `pivot`).

---

## 🧮 Fórmula Utilizada

A distância de Manhattan entre dois pontos \( P_1(x_1, y_1) \) e \( P_2(x_2, y_2) \) é dada por:

\[
d = |x_1 - x_2| + |y_1 - y_2|
\]

Neste caso:
- \( x \) = latitude norte (**LAT_N**)  
- \( y \) = longitude oeste (**LONG_W**)  

---

## 🚀 Como Executar

1. Clone este repositório no seu ambiente local ou Databricks.  
2. Crie a tabela `Station` com os dados simulados (12 cidades de exemplo).  
3. Execute o notebook no Databricks para gerar a matriz de distâncias.  

---

## 📊 Exemplo de Saída

| city_a     | Anchorage | Seattle | San Francisco | Los Angeles | Denver | ... |
|------------|-----------|---------|---------------|-------------|--------|-----|
| Anchorage  | 0.0       | 27.56   | 39.73         | 42.12       | 66.11  | ... |
| Seattle    | 27.56     | 0.0     | 10.22         | 13.55       | 25.33  | ... |
| San Juan   | 95.44     | 72.22   | 65.19         | 68.91       | 85.77  | ... |
| ...        | ...       | ...     | ...           | ...         | ...    | ... |

---

## 🛠️ Tecnologias Utilizadas

- [Databricks Free Edition](https://community.cloud.databricks.com/)  
- [PySpark](https://spark.apache.org/docs/latest/api/python/)  
- SQL (para consultas e manipulação de dados)  

---

## ✨ Funcionalidades Futuras

- Adicionar cálculo de **distância euclidiana** (linha reta).  
- Suporte para **datasets maiores** (100+ cidades).  
- Visualização gráfica do mapa com distâncias.  

---

## 👨‍💻 Autor

Projeto desenvolvido por **[Pedro Cordeiro]** ✨  
📬 Entre em contato para dúvidas ou sugestões!
