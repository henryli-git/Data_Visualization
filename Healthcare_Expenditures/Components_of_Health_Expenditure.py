import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Health_systems.csv')
df = df[['Country_Region', 'Health_exp_public_pct_2016', 'Health_exp_out_of_pocket_pct_2016']].dropna()
df['Health_exp_other_pct_2016'] = 100 - df['Health_exp_public_pct_2016'] - df['Health_exp_out_of_pocket_pct_2016']
df = df.sort_values('Health_exp_public_pct_2016', axis=0, ascending=True)

x = df['Country_Region']
y1 = df['Health_exp_public_pct_2016']
y2 = df['Health_exp_out_of_pocket_pct_2016']
y3 = df['Health_exp_other_pct_2016']
font = {'fontname': 'Arial Black', 'color': '#453d34'}

fig, ax = plt.subplots(figsize=(16, 9))
ax.set_facecolor('#000000')
ax.tick_params(axis='x', bottom=False, pad=0)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.bar(x, y1, label='Public', color='#584d42')
plt.bar(x, y2, bottom=y1, label='Out of Pocket', color='#12a303')
plt.bar(x, y3, bottom=y1 + y2, label='Other', color='#95d9f4')
plt.title('Components of Health Expenditure by Country in 2016', **font, fontsize=20)
plt.xticks(rotation=90, color='#453d34', fontsize=8)
plt.ylabel('Health Expenditure Share (%)', **font, fontsize=13)
plt.yticks(**font)

handles, labels = ax.get_legend_handles_labels()
ax.legend(reversed(handles), reversed(labels), loc=(0.89, 0.68), prop={'family': 'Arial Black'}, fontsize=9)

plt.margins(x=0)
plt.tight_layout()
plt.savefig('Components_of_Health_Expenditure_graph.png', ppi=300)
plt.show()
