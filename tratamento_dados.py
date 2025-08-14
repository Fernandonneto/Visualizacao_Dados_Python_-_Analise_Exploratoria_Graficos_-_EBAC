
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_csv('ecommerce_preparados.csv')
print(df.head(20).to_string())
print(df.tail(20).to_string())

# Preenche valores nulos com a média da coluna de "Qtd_Vendidos_Cod"
df['Qtd_Vendidos_Cod'] = df['Qtd_Vendidos_Cod'].fillna(df['Qtd_Vendidos_Cod'].mean())

# Retirar valores nulos do desconto
df = df.dropna(subset=['Desconto'])

# Retirar valores nulos da "Nota"
df = df.dropna(subset=['Nota'])

# Retirar valores nulos da "Gênero"
df = df.dropna(subset=['Gênero'])

# Preenche valores nulos com a média da coluna de "Preço"
df['Preço'] = df['Preço'].fillna(df['Preço'].mean())

print(df.head(20).to_string())
df.to_csv('ecommerce_tratados.csv', index = False)
