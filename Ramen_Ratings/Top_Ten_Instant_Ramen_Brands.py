import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Ramen_Ratings.csv')

df['Top Ten'] = df['Top Ten'].astype(str)
df['Year'] = df['Top Ten'].str.split(' ').apply(lambda x: x[0])
df['Rank'] = df['Top Ten'].str.split('#').apply(lambda x: x[-1])
df[['Rank', 'Year']] = df[['Rank', 'Year']].replace(['\n', 'nan'], 99).astype(int)
df = df[df['Rank'] != 99]

plt.style.use('Solarize_Light2')
plt.figure(figsize=(16, 9))
sns.scatterplot(df['Brand'], df['Rank'], style=df['Year'], s=100, color='#b17c5a')
plt.title('Top Ten Instant Ramen Brands', color='#5a7078', fontsize=20)
plt.tick_params(left=False)
plt.xticks(rotation=45, color='#b17c5a', ha='right', fontsize=12)
plt.xlabel(None)
plt.yticks(np.arange(1, 11, 1), fontsize=14)
plt.ylabel('Rank# (Lower is Better)', color='#b17c5a', fontsize=13)
plt.gca().invert_yaxis()
plt.legend(loc='best', shadow=True, fontsize=12)
plt.tight_layout()
plt.savefig('Top_Ten_Instant_Ramen_Brands_graph.png', dpi=300)
plt.show()
