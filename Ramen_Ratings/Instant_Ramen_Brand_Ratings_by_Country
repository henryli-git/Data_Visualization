import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Ramen_Ratings.csv')
df['Country'] = df['Country'].str.replace('United States', 'USA')
df['Stars'] = df['Stars'].str.replace('Unrated', '100')
df['Stars'] = df['Stars'].astype(float)
df = df[df['Stars'] != 100]
df = df.sort_values(by='Country')

fig = plt.figure(figsize=(16, 9))
plt.style.use('Solarize_Light2')
sns.boxplot(df['Country'], df['Stars'], palette='YlOrBr')

plt.title('Instant Ramen Brand Ratings by Country', fontweight='bold', fontsize=20)
plt.ylabel('Rating (Higher is Better)', fontsize=14, labelpad=10)
plt.yticks(fontsize=12)
plt.xlabel(None)
plt.xticks(rotation=90, fontsize=11)
plt.tight_layout()
plt.savefig('Instant_Ramen_Brand_Ratings_by_Country_graph.png', dpi=300)
plt.show()
