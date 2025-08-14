
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ecommerce_tratados.csv')
print(df.head(20).to_string())

# Gráfico de Dispersão
plt.figure(figsize = (10,6))
sns.scatterplot(x = 'Qtd_Vendidos_Cod', y = 'Preço', data = df, hue = 'Qtd_Vendidos_Cod',
palette = 'viridis', legend = 'brief', s = 80, edgecolor = 'w')
plt.title('Relação entre quantidade vendida de produtos e preços', fontweight='bold')
plt.xlabel('Quantidade Vendida')
plt.ylabel('Preço (R$)')
plt.show()

# Mapa de Calor
corr = df[['Desconto', 'Qtd_Vendidos_Cod']].corr()
plt.subplot(2, 2, 3)
sns.heatmap(corr, annot = True, cmap = 'RdPu')
plt.title('Correlação de descontos e vendas de produtos', fontweight='bold')
plt.tight_layout()
plt.show()

# Gráfico de Barra
plt.figure(figsize = (10,6))
df['Nota'].value_counts().plot(kind = 'bar', color = '#5c1de0')
plt.title('Distribuição das avaliações dos produtos', fontweight='bold')
plt.xlabel('Notas dos produtos')
plt.ylabel('Quantidade')
plt.xticks(rotation = 0)
plt.show()

# Gráfico de Pizza
cores = ['#6a0dad', '#8a2be2', '#ff69b4', '#ff7f50', '#ff6347', '#ff0000']
genero_counts = df['Gênero'].value_counts().nlargest(6)

x = genero_counts.index
y = genero_counts.values

plt.figure(figsize = (10,6))
plt.pie(y, labels = x, colors = cores, autopct = '%.1f%%', startangle = 90)
plt.title('Participação percentual dos gêneros dos produtos', fontweight='bold')
plt.axis('equal')
plt.show()

# Gráfico de Densidade
plt.figure(figsize = (10,6))
sns.kdeplot(df['Preço'], fill = True, color = '#e01d4d')
plt.title('Distribuição de densidade dos preços dos produtos', fontweight='bold')
plt.xlabel('Preços dos produtos (R$)')
plt.show()