```markdown
# Análise de Dados de Vendas para a Empresa XYZ

## Descrição do Projeto

Este projeto foi desenvolvido para a empresa XYZ, uma rede de lojas de varejo de produtos para casa e jardim. O objetivo principal é analisar os dados de vendas para entender melhor o perfil dos clientes e as tendências de vendas por categoria de produto e região geográfica, visando a melhoria dos resultados financeiros. As análises e recomendações são direcionadas à equipe de gerenciamento.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
desafio-data-analytics/
├── analises_python/                  # Scripts Python para análise e pré-processamento de dados
│   ├── Base-Dados-Desafio-D&A-01.xlsx # Base de dados original utilizada
│   ├── df_completo.csv               # DataFrame resultante do processamento em Python
│   ├── preparacao_dados.py           # Script para carregar, unir e pré-processar os dados
│   ├── perfil_demografico.py         # Script para análise do perfil demográfico dos clientes
│   ├── categoria_mais_vendida.py     # Script para identificar categorias de produtos mais/menos vendidas
│   ├── vendas_sazonais.py            # Script para analisar a relação entre vendas e época do ano
│   ├── regiao_geografica.py          # Script para analisar tendências de vendas por região geográfica
│   ├── relacao_idade_categoria.py    # Script para analisar a correlação entre idade e categorias de produtos
│   └── graficos.py                   # Script para gerar visualizações em Python
├── graficos_gerados_python/          # Imagens dos gráficos gerados pelas análises em Python
│   ├── correlacao_idade_categoria.png
│   ├── distribuicao_idade.png
│   ├── vendas_por_categoria.png
│   ├── vendas_por_estado.png
│   └── vendas_por_mes.png
├── desafio_data_analytics.pbix       # Arquivo do projeto Power BI Desktop com o dashboard
└── README.md                         # Este arquivo de documentação
```

## Metodologia

O projeto seguiu uma abordagem em duas etapas:

1.  **Análise e Pré-processamento com Python:** Utilização da linguagem Python e da biblioteca `pandas` para carregar e transformar os dados da `Base-Dados-Desafio-D&A-01.xlsx`. Scripts específicos foram desenvolvidos para responder às perguntas de negócio propostas, gerando insights e visualizações preliminares com `matplotlib` e `seaborn`.
2.  **Visualização e Dashboard com Power BI:** Criação de um dashboard interativo no Power BI Desktop, utilizando a `Base-Dados-Desafio-D&A-01.xlsx` diretamente como fonte de dados. O dashboard consolida os principais KPIs e visualizações, permitindo uma exploração dinâmica e intuitiva dos resultados.

## Análise de Dados com Python

A fase de Python focou na exploração e preparação dos dados. O script `preparacao_dados.py` foi responsável por:

*   Carregar as abas `VENDAS` e `PRODUTOS` da `Base-Dados-Desafio-D&A-01.xlsx`.
*   Realizar a junção (`merge`) das tabelas `df_vendas` e `df_produtos` usando a coluna `PRODUTO`.
*   Converter a coluna `DATA` para o formato datetime.
*   Exportar o DataFrame resultante para `df_completo.csv` para uso posterior (embora no Power BI a fonte original tenha sido utilizada).

Os demais scripts na pasta `analises_python/` foram utilizados para gerar as análises e gráficos correspondentes às perguntas de negócio, cujos resultados estão em `graficos_gerados_python/`.

## Dashboard no Power BI Desktop

O dashboard interativo (`desafio_data_analytics.pbix`) foi desenvolvido no Power BI Desktop, utilizando a `Base-Dados-Desafio-D&A-01.xlsx` como fonte de dados principal. A modelagem de dados e a criação de medidas DAX foram realizadas para suportar as visualizações e KPIs apresentados.

### Modelagem de Dados

No Power BI, a `Base-Dados-Desafio-D&A-01.xlsx` foi carregada. As tabelas foram estruturadas da seguinte forma, conforme a organização visual do Power BI:

*   **`fVendas`:** Representa a tabela de fatos de vendas, contendo os dados transacionais.
*   **`dProdutos`:** Tabela de dimensão para produtos, contendo informações únicas de `PRODUTO` e `CATEGORIA`.
*   **`dCalendario`:** Tabela de dimensão de tempo, criada em DAX para análises temporais (Ano, Mês, Nome do Mês, etc.).
*   **`Última_Atualização`:** Tabela de metadados para exibir a data da última atualização.

Os relacionamentos entre `fVendas` e as tabelas de dimensão (`dProdutos`, `dCalendario`) foram estabelecidos para permitir a filtragem e agregação corretas dos dados.

### Medidas DAX e KPIs

As seguintes medidas DAX foram implementadas para calcular os KPIs exibidos no dashboard:

*   **Total de Vendas:** `SUM(fVendas[Total de Itens Vendidos])`
    *   *KPI:* Quantidade total de itens vendidos.
*   **Número de Pedidos:** `COUNTROWS(fVendas)`
    *   *KPI:* Número total de transações ou registros de vendas.
*   **Clientes Únicos:** `DISTINCTCOUNT(fVendas[CLIENTE])`
    *   *KPI:* Quantidade de clientes distintos que realizaram compras.
*   **Quantidade Média p/ Cliente:** `DIVIDE([Total de Itens Vendidos], [Clientes Únicos], 0)`
    *   *KPI:* Média de itens vendidos por cliente único.

### Visualizações Chave

O dashboard apresenta as seguintes visualizações, que respondem diretamente às perguntas de negócio:

*   **Total de Vendas, Número de Pedidos, Clientes Únicos, Quantidade Média p/ Cliente:** Exibidos como cartões para um resumo rápido dos principais KPIs.
*   **Categoria Mais Vendida:** Gráfico de rosca (`Doughnut Chart`) mostrando a distribuição da `Total de Itens Vendidos` por `CATEGORIA`.
*   **Perfil Demográfico - Distribuição por Idade:** Gráfico de colunas que visualiza a contagem de clientes por faixas etárias (bins de idade).
*   **Vendas por Mês (Tendência Anual):** Gráfico de linha que exibe a `Total de Itens Vendidos` ao longo dos meses, revelando padrões sazonais.
*   **Vendas por Estado:** Gráfico de barras horizontais que compara a `Total de Itens Vendidos` entre os diferentes estados.
*   **Relação Idade vs Categoria de Produtos:** Tabela ou matriz que detalha a `Total de Itens Vendidos` por faixa etária e categoria de produto, permitindo identificar preferências.

Segmentações de dados (slicers) para `Estado`, `Categoria`, `Faixa Etária` e `Ano/Mês` estão presentes para permitir uma análise interativa e detalhada.

## Como Utilizar o Projeto

1.  **Python:** Os scripts na pasta `analises_python/` podem ser executados para replicar as análises e gerar o arquivo `df_completo.csv` e os gráficos PNG na pasta `graficos_gerados_python/`.
2.  **Power BI:** Abra o arquivo `desafio_data_analytics.pbix` com o Power BI Desktop. Certifique-se de que a `Base-Dados-Desafio-D&A-01.xlsx` esteja acessível no mesmo local ou atualize a fonte de dados no Power Query, se necessário. Explore as páginas do relatório e utilize os filtros para interagir com os dados.

## Conclusão e Recomendações

Este projeto oferece à empresa XYZ uma visão abrangente de seus dados de vendas. Os insights obtidos podem ser utilizados para:

*   **Otimização de Marketing:** Direcionar campanhas com base no perfil demográfico e nas preferências de produtos por idade e região.
*   **Gestão de Estoque:** Planejar o estoque e promoções com base nas tendências sazonais de vendas.
*   **Estratégia de Expansão:** Avaliar o desempenho por estado para identificar oportunidades de crescimento ou áreas que necessitam de atenção.

As análises destacam a importância de categorias como `Utilidades Domésticas` e `Limpeza`, enquanto `Jardinagem` aparece com menor volume de vendas. A sazonalidade é evidente, com picos em certos meses e quedas em outros. Recomenda-se aprofundar a investigação sobre os fatores que impulsionam essas tendências e, futuramente, considerar a inclusão de dados de valor monetário para análises financeiras mais completas.
```
