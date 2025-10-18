import pandas as pd

df_completo = pd.read_csv("df_completo.csv")

vendas_por_estado = (
    df_completo.groupby("ESTADO")["QUANTIDADE_VENDIDA"]
    .sum()
    .sort_values(ascending=False)
)

print("## Tendência de Vendas por Região Geográfica")
print("### Vendas por Estado")
print(vendas_por_estado.to_markdown())
