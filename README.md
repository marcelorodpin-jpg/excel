# Agrupador de Dados do Excel 📊

Este projeto é uma ferramenta em Python desenvolvida para automatizar a leitura de planilhas eletrônicas, agrupar dados por categorias específicas e realizar a soma automática de seus valores.

## 🚀 Funcionalidades

* **Leitura Automatizada:** Importação rápida de dados de arquivos Excel (`.xlsx`).
* **Agrupamento Inteligente:** Consolidação de linhas com base em colunas de identificação.
* **Cálculo de Métricas:** Soma matemática automática dos valores financeiros ou numéricos associados.
* **Exportação:** Geração de um novo arquivo consolidado para tomada de decisões.

## 🛠️ Tecnologias Utilizadas

* **Python 3** (Linguagem base)
* **Pandas** (Biblioteca principal para manipulação e análise de dados)
* **Openpyxl** (Motor de integração para leitura/escrita de arquivos Excel)

## 📦 Como Instalar e Rodar o Projeto

### Pré-requisitos
Certifique-se de ter o **Python** instalado em sua máquina.

### 1. Clonar o repositório
```bash
git clone https://github.com
cd nome-do-seu-repositorio
```

### 2. Instalar as dependências
```bash
pip install pandas openpyxl
```

### 3. Executar a aplicação
Coloque a sua planilha na pasta raiz do projeto e execute:
```bash
python main.py
```

## 📝 Exemplo de Uso

### Entrada (Dados Originais):

| Categoria | Valor |
| :--- | :--- |
| Eletrônicos | 1500 |
| Roupas | 300 |
| Eletrônicos | 500 |

### Saída (Dados Agrupados):

| Categoria | Valor |
| :--- | :--- |
| Eletrônicos | 2000 |
| Roupas | 300 |

## ✒️ Autor

* **[Marcelo Rodrigues]** 
