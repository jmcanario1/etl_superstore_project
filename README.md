# 🛠️ Projeto de Estudo: Pipeline ETL com Python

Este projeto foi criado com o objetivo de praticar e aprender sobre **ETL (Extract, Transform, Load)** utilizando Python e pandas, com base em um dataset de vendas similar ao Superstore (contendo informações de pedidos, clientes, produtos, lucros, descontos, etc).

---

## 📌 Objetivo

O objetivo principal é construir um **pipeline ETL simples e bem estruturado** que possa:

- Extrair dados de um arquivo CSV
- Transformar os dados brutos (limpeza, enriquecimento, novas colunas)
- Salvar os dados limpos e prontos para análise

Este projeto é **educacional**, ideal para quem está começando a aprender sobre **Data Engineering**, **Data Science**, ou **Análise de Dados com Python**.

---

## 📁 Estrutura do Projeto

```
etl_superstore_project/
├── data/
│   ├── raw/
│   └── processed/
├── etl/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── etl_pipeline.py
├── requirements.txt
└── README.md
```

---

## 🔧 Tecnologias Utilizadas

- Python 3.9+
- Pandas
- (opcional) SQLite ou Parquet (para etapas futuras)

---

## 🚀 Como Executar

1. **Clone o repositório**

git clone https://github.com/jmcanario1/etl_superstore_project.git
cd etl_superstore_project


2. **Crie um ambiente virtual (opcional, mas recomendado)**

python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows


3. **Instale as dependências**

pip install -r requirements.txt


4. **Coloque o arquivo de dados em data/raw/superstore.csv**


5. **Execute o pipeline**

python etl_pipeline.py


🔄 Funcionalidades do Pipeline
Conversão de datas (Order Date, Ship Date)

Criação de colunas derivadas:

Tempo de envio (em dias)

Margem de lucro

Classificação de lucro (Alto, Moderado, Negativo)

Tratamento de colunas (snake_case)

Remoção de dados inválidos (ex: entregas com tempo negativo)

Salvamento do dataset limpo em CSV

📈 Próximas Melhorias
Salvar os dados transformados em formato Parquet ou banco de dados (SQLite/PostgreSQL)

Adicionar testes automatizados (pytest)

Criar um dashboard com Streamlit ou Dash

Automatizar a execução com Airflow ou Prefect

🧠 Aprendizados
Este projeto é parte da minha jornada de aprendizado em:

Engenharia de dados

Processamento de dados com Python

Estruturação de pipelines ETL

Boas práticas em projetos de dados

📬 Contato
Caso queira trocar ideias, sugestões ou dúvidas:

Nome: [João Marcelo Canário]

Email: [joaomarcelocanariodev@gmail.com]

LinkedIn: [https://www.linkedin.com/in/joaomarcelocanario/]

Nota: Este projeto é apenas para fins educacionais e não deve ser usado em produção sem adaptações apropriadas.