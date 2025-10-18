import pandas as pd

df_completo = pd.read_csv("df_completo.csv")

perfil_idade = df_completo["IDADE"].describe()

perfil_estado = df_completo["ESTADO"].value_counts()

print("## Perfil Demográfico dos Clientes")
print("### Distribuição de Idade")
print(perfil_idade.to_markdown())
print("\n### Distribuição por Estado")
print(perfil_estado.to_markdown())
