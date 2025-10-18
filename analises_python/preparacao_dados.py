import pandas as pd

df_vendas = pd.read_excel("Base-Dados-Desafio-D&A-01.xlsx", sheet_name="VENDAS")
df_produtos = pd.read_excel("Base-Dados-Desafio-D&A-01.xlsx", sheet_name="PRODUTOS")

df_completo = pd.merge(df_vendas, df_produtos, on="PRODUTO", how="left")

df_completo["DATA"] = pd.to_datetime(df_completo["DATA"])

df_completo.to_csv("df_completo.csv", index=False)
