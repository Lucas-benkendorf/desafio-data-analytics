#  Análise de Dados de Vendas - Empresa XYZ

##  Descrição do Projeto

Este projeto foi desenvolvido para a **Empresa XYZ**, uma rede de lojas de varejo especializada em produtos para **casa e jardim**. O objetivo principal é analisar os dados de vendas para entender melhor o perfil dos clientes e identificar tendências por categoria de produto e região geográfica, visando a **melhoria dos resultados financeiros**.

---

##  Estrutura do Projeto
desafio-data-analytics/
├──  analises_python/ # Scripts Python para análise e pré-processamento
│ ├──  Base-Dados-Desafio-D&A-01.xlsx
│ ├──  df_completo.csv
│ ├──  preparacao_dados.py
│ ├──  perfil_demografico.py
│ ├──  categoria_mais_vendida.py
│ ├──  vendas_sazonais.py
│ ├──  regiao_geografica.py
│ ├──  relacao_idade_categoria.py
│ └──  graficos.py
├──  graficos_gerados_python/ # Visualizações geradas em Python
│ ├──  correlacao_idade_categoria.png
│ ├──  distribuicao_idade.png
│ ├──  vendas_por_categoria.png
│ ├──  vendas_por_estado.png
│ └──  vendas_por_mes.png
├──  desafio_data_analytics.pbix # Dashboard interativo no Power BI
└── README.md # Documentação do projeto


---

##  Metodologia

O projeto foi desenvolvido em **duas etapas principais**:

### 1. **Análise e Pré-processamento com Python**
- Utilização das bibliotecas `pandas`, `matplotlib` e `seaborn`
- Carregamento, transformação e limpeza dos dados
- Geração de insights e visualizações preliminares

### 2. **Visualização e Dashboard com Power BI**
- Criação de relatório interativo e intuitivo
- Desenvolvimento de medidas DAX para KPIs
- Modelagem dimensional para análise multidimensional

---

##  Análise de Dados com Python

###  Pré-processamento
O script `preparacao_dados.py` realizou:
- Carregamento das abas `VENDAS` e `PRODUTOS`
- Junção das tabelas usando a coluna `PRODUTO`
- Conversão da coluna `DATA` para datetime
- Exportação do DataFrame consolidado

###  Análises Realizadas
- **Perfil Demográfico**: Distribuição etária dos clientes
- **Categorias Mais Vendidas**: Identificação de produtos com melhor performance
- **Sazonalidade**: Análise temporal das vendas
- **Distribuição Geográfica**: Vendas por estado/região
- **Relação Idade vs Categoria**: Preferências por faixa etária

---

##  Dashboard Power BI

###  Modelagem de Dados
| Tabela | Tipo | Descrição |
|--------|------|-----------|
| `fVendas` | Fato | Transações de vendas |
| `dProdutos` | Dimensão | Catálogo de produtos |
| `dCalendario` | Dimensão | Hierarquia temporal |
| `Última_Atualização` | Metadados | Data de atualização |

###  KPIs Principais
| KPI | Fórmula DAX | Descrição |
|-----|-------------|-----------|
| **Total de Vendas** | `SUM(fVendas[Total de Itens Vendidos])` | Volume total de itens |
| **Número de Pedidos** | `COUNTROWS(fVendas)` | Quantidade de transações |
| **Clientes Únicos** | `DISTINCTCOUNT(fVendas[CLIENTE])` | Clientes distintos |
| **Média por Cliente** | `[Total Vendas] / [Clientes Únicos]` | Volume médio por cliente |

###  Visualizações Implementadas
-  **Cartões de KPI** - Resumo executivo
-  **Gráfico de Rosca** - Categorias mais vendidas
-  **Gráfico de Colunas** - Distribuição por idade
-  **Gráfico de Linha** - Tendência mensal de vendas
-  **Mapa/Mapa de Árvore** - Vendas por estado
-  **Matriz** - Relação idade vs categoria

###  Filtros Interativos
- **Estado** 
- **Categoria** 
- **Faixa Etária** 
- **Período** 

---

##  Como Utilizar

### Para replicar as análises em Python:
```bash
cd analises_python
python preparacao_dados.py
python perfil_demografico.py
