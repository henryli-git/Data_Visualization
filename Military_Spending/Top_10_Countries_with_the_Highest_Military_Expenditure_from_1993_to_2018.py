import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets_376235_731395_Military Expenditure.csv')
df = df[df['Type'] == 'Country']
df = df.sort_values('2018', ascending=False)
df_years = df.loc[:, '1993': '2018']
df_years = df_years / 1_000_000_000
df = pd.concat([df['Name'], df_years], axis=1)[:10]
df = df.set_index('Name')
df = df.T

colors = ["#806364",
          "#720000",
          "#fff6de",
          "#dfbec3",
          "#bddff0",
          "#000000",
          "#e0bb19",
          "#00498e",
          "#602b43",
          "#ffe0bd"]

plt.style.use('seaborn')
plt.rcParams.update({'text.color': '#400000',
                     'axes.labelcolor': '#400000',
                     'font.family': 'Lucida Grande'})

ax = df.plot.area(figsize=(16, 9), color=colors, alpha=0.65)
ax.set_yticklabels([f'{int(x):,}' for x in ax.get_yticks().tolist()])
ax.set_ylim([0, 1400])
ax.set_facecolor('#cc99a2')

handles, labels = ax.get_legend_handles_labels()
ax.legend(reversed(handles), reversed(labels), fontsize=11)

plt.setp(ax.get_yticklabels()[0], visible=False)
plt.title('Top 10 Countries with the Highest Military Expenditure from 1993 to 2018', fontsize=20)
plt.xticks(fontsize=11, color='#400000')
plt.ylabel('Expenditure in Billions (USD)', fontsize=15)
plt.yticks(fontsize=11, color='#400000')
plt.grid(alpha=.6)
plt.margins(x=0)
plt.savefig('Top_10_Countries_with_the_Highest_Military_Expenditure_from_1993_to_2018_graph.png', ppi=300)
plt.show()
