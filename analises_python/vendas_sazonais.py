import pandas as pd

df_completo = pd.read_csv("df_completo.csv")
df_completo["DATA"] = pd.to_datetime(df_completo["DATA"])

df_completo["MES"] = df_completo["DATA"].dt.month

vendas_por_mes = df_completo.groupby("MES")["QUANTIDADE_VENDIDA"].sum().sort_index()

print("## Relação entre Vendas e Época do Ano")
print("### Vendas por Mês")
print(vendas_por_mes.to_markdown())
