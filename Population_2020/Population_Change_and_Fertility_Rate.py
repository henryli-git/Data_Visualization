import pandas as pd
import matplotlib.pyplot as plt
from adjustText import adjust_text

df = pd.read_csv('population_by_country_2020.csv')
df = df.sort_values('Population (2020)', ascending=False)
df = df[:50]
df = df[~df.isin(['N.A.'])]
df = df.fillna(0)
df['Fert. Rate'] = df['Fert. Rate'].astype(float)
df['Yearly Change'] = df['Yearly Change'].str.split('%', expand=True)
df['Yearly Change'] = df['Yearly Change'].astype(float)

x = df['Yearly Change']
y = df['Fert. Rate']
z = df['Country (or dependency)'].values
plt.style.use('seaborn-dark')
plt.rcParams['font.family'] = 'Meiryo'
plt.figure(figsize=(16, 9))
plt.scatter(x, y, color='#228B22', alpha=.8)
texts = [plt.text(x[i], y[i], text, color='#0887BE') for i, text in enumerate(z)]
adjust_text(texts, arrowprops=dict(arrowstyle='-', color='#8B4513', alpha=.7))
plt.title("Population Change and Fertility Rate for the 50 Most Populous Countries in 2020", fontsize=18,
          fontweight='bold', color='#045F86')
plt.xlabel('Annual Population Change (%)', fontsize=15, fontweight='bold', color='#045F86')
plt.xticks(fontsize=12, color='#045F86')
plt.ylabel('Fertility Rate', fontsize=15, fontweight='bold', color='#045F86')
plt.yticks(fontsize=12, color='#045F86')
plt.gca().get_xticklabels()[1].set_color('red')
plt.tight_layout()

plt.savefig('Population_Change_and_Fertility_Rate_graph.png', ppi=600)
plt.show()
