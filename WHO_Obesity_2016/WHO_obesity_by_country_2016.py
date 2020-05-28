'''Obesity Among Adults Around the World in 2016'''

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('dark_background')
plt.tight_layout()

df = pd.read_csv('WHO_obesity_by_country_2016.csv')
df.rename(columns={'Unnamed: 0': 'Country'}, inplace=True)
df.dropna(inplace=True)

country = df['Country']
both = df['Both.sexes']

plt.barh(country, both,
         color=['#CD5C5C', '#00BFFF', '#FF0000', '#FA8072', '#6495ED', '#F08080', '#FF6347', '#0000FF', '#B22222'])

plt.title('Obesity Among Adults Around the World in 2016', size=10)
plt.tick_params(axis='y', which='major', labelsize=1.3)
plt.xticks(size=6.5)
plt.xlabel('% Obese (BMI ≥ 30)', size=8)
plt.savefig('WHO_obesity_by_country_2016_graph.pdf')
plt.show()
