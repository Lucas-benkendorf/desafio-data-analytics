import pandas as pd

df_completo = pd.read_csv("df_completo.csv")

vendas_por_categoria = (
    df_completo.groupby("CATEGORIA")["QUANTIDADE_VENDIDA"]
    .sum()
    .sort_values(ascending=False)
)

print("## Categorias de Produtos Mais e Menos Vendidas")
print("### Vendas por Categoria de Produto")
print(vendas_por_categoria.to_markdown())
