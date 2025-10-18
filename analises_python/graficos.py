import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

output_dir = os.path.join(base_dir, "graficos_gerados_python")

os.makedirs(output_dir, exist_ok=True)

df_completo = pd.read_csv(os.path.join(base_dir, "df_completo.csv"))

plt.figure(figsize=(10, 6))
sns.histplot(df_completo["IDADE"], bins=5, kde=True)
plt.title("Distribuição de Idade dos Clientes")
plt.xlabel("Idade")
plt.ylabel("Frequência")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "distribuicao_idade.png"))
plt.close()

vendas_por_categoria = (
    df_completo.groupby("CATEGORIA")["QUANTIDADE_VENDIDA"]
    .sum()
    .sort_values(ascending=False)
)
plt.figure(figsize=(12, 7))
sns.barplot(
    x=vendas_por_categoria.index, y=vendas_por_categoria.values, palette="viridis"
)
plt.title("Vendas por Categoria de Produto")
plt.xlabel("Categoria de Produto")
plt.ylabel("Quantidade Vendida")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "vendas_por_categoria.png"))
plt.close()

df_completo["DATA"] = pd.to_datetime(df_completo["DATA"])
df_completo["MES"] = df_completo["DATA"].dt.month
vendas_por_mes = df_completo.groupby("MES")["QUANTIDADE_VENDIDA"].sum().sort_index()
plt.figure(figsize=(12, 7))
sns.lineplot(x=vendas_por_mes.index, y=vendas_por_mes.values, marker="o")
plt.title("Vendas por Mês")
plt.xlabel("Mês")
plt.ylabel("Quantidade Vendida")
plt.xticks(range(1, 13))
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "vendas_por_mes.png"))
plt.close()

vendas_por_estado = (
    df_completo.groupby("ESTADO")["QUANTIDADE_VENDIDA"]
    .sum()
    .sort_values(ascending=False)
)
plt.figure(figsize=(12, 7))
sns.barplot(x=vendas_por_estado.index, y=vendas_por_estado.values, palette="viridis")
plt.title("Vendas por Estado")
plt.xlabel("Estado")
plt.ylabel("Quantidade Vendida")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "vendas_por_estado.png"))
plt.close()

correlacao_idade_categoria = (
    df_completo.groupby(["IDADE", "CATEGORIA"])["QUANTIDADE_VENDIDA"]
    .sum()
    .unstack(fill_value=0)
)
plt.figure(figsize=(14, 8))
sns.heatmap(correlacao_idade_categoria, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Correlação entre Idade dos Clientes e Categorias de Produtos")
plt.xlabel("Categoria de Produto")
plt.ylabel("Idade do Cliente")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "correlacao_idade_categoria.png"))
plt.close()

print(f"Gráficos salvos em: {output_dir}")
