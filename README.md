# Visualização de Dados com Python: Análise Exploratória com Gráficos

Este projeto foi desenvolvido como parte de uma atividade semi-autônoma, atendendo aos requisitos mínimos necessários para avaliação do modulo ''Python: Visualização de Dados'' do curso de Ciência de Dados da EBAC, utilizando as bibliotecas, pandas para manipular os dados, matplotlib para criar gráficos básicos e seaborn para criar gráficos mais avançados e atraentes. Essas bibliotecas se integram bem, permitindo criar visualizações de dados de alta qualidade e personalizadas para o projeto. As derradeiras instruções e critérios exigidos para a elaboração deste projeto estão descritos no arquivo “Profissão Cientista de Dados M10 Pratique.ipynb”.

A seguir, são apresentados os conceitos dos gráficos utilizados no projeto, juntamente com uma breve explicação sobre o que cada um está analisando no contexto dos dados e como foi tratado.

- **Gráfico de dispersão:** 
  - O gráfico de dispersão representa visualmente a relação entre duas variáveis numéricas por meio de pontos em um plano cartesiano, onde cada ponto corresponde a uma observação única. Essa visualização é útil para identificar correlações entre variáveis e detectar valores atípicos (outliers) com facilidade. 

   - Nesta atividade, o gráfico de dispersão analisa a relação entre o preço dos produtos e a quantidade vendida, permitindo observar se há uma tendência de venda maior entre produtos mais baratos, além de destacar possíveis valores fora do padrão. Assim, ele auxilia na compreensão do impacto do preço sobre as vendas.

  - Para garantir a qualidade da análise, valores nulos na coluna "Qtd_Vendidos_Cod" foram preenchidos com a média da respectiva coluna, evitando a perda de informações importantes e mantendo a consistência dos dados.


- **Mapa de calor:** 
  - Esse tipo de visualização utiliza cores para representar a intensidade dos valores em uma matriz, facilitando a identificação de padrões e correlações, especialmente quando se trabalha com grandes volumes de dados. 

  - No projeto, o mapa de calor analisa a relação entre o desconto aplicado e a quantidade de produtos vendidos, usando as cores para indicar a intensidade da correlação entre essas variáveis. Dessa forma, é possível visualizar rapidamente se existe uma associação significativa entre oferecer descontos e o aumento das vendas, facilitando a percepção de padrões e tendências em grandes conjuntos de dados.

  - Para garantir a qualidade da análise, foram removidas as linhas com valores nulos na coluna "Desconto", já que esses dados são essenciais e não podem ser substituídos facilmente sem comprometer a interpretação.


- **Gráfico de barra:** 
  - O gráfico de barras é uma ferramenta eficaz para comparar valores entre categorias, utilizando a altura ou comprimento das barras para visualizar frequências, médias ou totais em dados categóricos. 

  - No gráfico apresentado, analisa a relação entre a satisfação dos clientes e o desempenho comercial dos produtos, buscando identificar se há uma correlação entre o nível de avaliações e a qualidade do produto, ou seja, se os produtos com mais avaliações são de fato os melhores. Essa análise pode fornecer insights valiosos para entender melhor o comportamento dos clientes e otimizar a oferta de produtos.

  - Para garantir a precisão da análise, foram removidas as linhas sem avaliação na coluna "Nota", já que valores ausentes não contribuem para a avaliação dos produtos.


- **Gráfico de pizza:** 
  - O gráfico de pizza representa a proporção de cada categoria em relação ao total por meio de fatias de um círculo, sendo indicado para mostrar distribuições percentuais quando há poucas categorias. 
  
  - Neste contexto, o gráfico analisa a distribuição de produtos por gênero, destacando a participação percentual de cada grupo no total, com até seis categorias. Essa visualização facilita a comparação clara e rápida entre os diferentes gêneros dos produtos.

  - Para garantir a precisão da análise, foram eliminadas as linhas sem informação na coluna "Gênero", assegurando que os dados dessa categoria estejam completos e confiáveis.


- **Gráfico de densidade:** 
  - Esse tipo de visualização suaviza os dados, criando uma representação contínua e visualmente mais agradável da distribuição. O gráfico de densidade é especialmente útil para identificar padrões e tendências de forma intuitiva em grandes conjuntos de dados. 

  - Neste projeto, ele analisa a distribuição da quantidade de produtos vendidos, permitindo perceber as faixas de venda mais comuns e destacar produtos com vendas fora do padrão, tanto muito abaixo quanto muito acima do esperado.

  - Para garantir a integridade da análise, os valores nulos na coluna "Preço" foram substituídos pela média, evitando a perda de dados e mantendo o equilíbrio das informações.

Em suma este projeto, parte de uma atividade semi-autônoma do módulo "Python: Visualização de Dados" do curso de Ciência de Dados da EBAC, cumpriu os requisitos descritos no arquivo “Profissão Cientista de Dados M10 Pratique.ipynb”. Foram utilizados diversos tipos de gráficos para analisar os dados: o gráfico de dispersão explorou a relação entre preço e quantidade vendida; o mapa de calor revelou a correlação entre descontos e vendas; o gráfico de barras comparou vendas por faixa de nota dos produtos; o gráfico de pizza mostrou a distribuição percentual dos produtos por gênero; e o gráfico de densidade identificou padrões e anomalias na quantidade vendida. Cada visualização ajudou a interpretar diferentes aspectos dos dados, facilitando a compreensão de tendências e padrões relevantes.
