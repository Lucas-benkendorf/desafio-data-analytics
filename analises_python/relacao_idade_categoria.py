import pandas as pd

df_completo = pd.read_csv("df_completo.csv")

correlacao_idade_categoria = (
    df_completo.groupby(["IDADE", "CATEGORIA"])["QUANTIDADE_VENDIDA"]
    .sum()
    .unstack(fill_value=0)
)

print("## Correlação entre Idade dos Clientes e Categorias de Produtos")
print(correlacao_idade_categoria.to_markdown())
