import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv('datasets_610579_1093011_chocolate.csv')
df = df.sort_values(by='country_of_bean_origin')
df['country_of_bean_origin'] = df['country_of_bean_origin'].str.title()

plt.figure(figsize=(16, 9))
plt.style.use('seaborn-darkgrid')
plt.rcParams.update({'text.color': '#2c1242',
                     'axes.labelcolor': '#2c1242',
                     'axes.facecolor': '#c3b2d2',
                     'xtick.color': '#2c1242',
                     'grid.color': '#cabdd6',
                     'font.family': 'Arial Rounded MT Bold'})

sns.boxplot(x=df['country_of_bean_origin'], y=df['rating'], palette='PuOr')

plt.title('Chocolate Bar Ratings by Country of Cocoa Bean Origin', fontweight='bold', fontsize=20)
plt.ylabel('Rating (Higher is Better)', fontsize=14, labelpad=5)
plt.yticks(fontsize=12)
plt.xlabel(None)
plt.xticks(rotation=90, fontsize=11)
plt.tight_layout()
plt.savefig('Chocolate_Bar_Ratings_by_Country_of_Cocoa_Bean_Origin.png', dpi=300)
plt.show()
