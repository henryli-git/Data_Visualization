import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Billionaires.csv')
df = df.nlargest(109, 'year')

plt.style.use('seaborn-darkgrid')
plt.rcParams["font.family"] = "Trajan Pro"
fig, ax = plt.subplots(figsize=(16,9))

palette = ["#ffb56c",
"#7e7ff1",
"#5edd4b",
"#d65ee1",
"#abe23c",
"#e85da8",
"#7ada6f",
"#bd8adb",
"#e4cd39",
"#6d9bdc",
"#cf2a16",
"#d68282",
"#80446e",
"#62a430",
"#e9d9f7",
"#b8c550",
"#00ffff",
"#bea04d",
"#7ce1e1",
"#d6926a",
"#7fd9b8",
"#8593ac",
"#bfd48c",
"#e2e015",
"#3782a8",
"#6ea361",
"#ff5a00"]
sns.set_palette(palette)

sns.lineplot(data=df, x='year', y='net_worth', hue='name', linewidth=3, palette=sns.color_palette(palette, 27))

handles, labels = ax.get_legend_handles_labels()
leg = ax.legend(handles=handles[1:], labels=labels[1:], bbox_to_anchor=(1.01, 0.91), loc=2, frameon=False, prop={'family':'Franklin Gothic Book', 'size': 12})
for line in leg.get_lines():
    line.set_linewidth(3)

plt.title('Top 10 Wealthiest by Year', fontsize=20)
plt.xticks(list(range(2009, 2020, 1)), size=11)
plt.xlabel('Year', labelpad=7, fontsize=14)
plt.yticks(size=11)
plt.ylabel('Net Worth in Billions U.S Dollars', fontsize=14)
plt.margins(x=0)
plt.tight_layout()
plt.savefig('Top_10_Wealthiest_by_Year_graph.png', ppi=300)
plt.show()


