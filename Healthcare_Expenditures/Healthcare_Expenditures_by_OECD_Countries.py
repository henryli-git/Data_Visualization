import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('OECD_Health_systems.csv')
df = df[['Country_Region', 'Health_exp_per_capita_USD_2016', 'Health_exp_pct_GDP_2016']].dropna()
df = df.sort_values('Health_exp_per_capita_USD_2016', ascending=True)

x = df['Health_exp_per_capita_USD_2016']
y = df['Country_Region']
z = df['Health_exp_pct_GDP_2016']
font = {'fontname': 'Arial Rounded MT Bold', 'color': '#326479'}
colors = [
    "#ff3662",
    "#ff747c",
    "#6a0004",
    "#a3000a",
    "#d9690d",
    "#441814",
    "#ffb4a1",
    "#5b372b",
    "#934700",
    "#ff9f57",
    "#633c00",
    "#ebc147",
    "#d8bf00",
    "#c9ce1e",
    "#405a00",
    "#bccc97",
    "#59e131",
    "#007e2c",
    "#01d766",
    "#72db92",
    "#006b57",
    "#00ac9a",
    "#018eae",
    "#94ceed",
    "#00436b",
    "#80bdff",
    "#739fff",
    "#0050a1",
    "#0250d4",
    "#000d93",
    "#9969ff",
    "#d1abff",
    "#7300be",
    "#880071",
    "#ff25ce",
    "#ff81c5",
    "#ce0085"]

fig, ax = plt.subplots(figsize=(16, 9))

plt.barh(y, x, color=colors, alpha=0.8)
for i, (v1, v2) in enumerate(zip(x, z)):
    plt.text(v1 + 25, i, f'{v1:,.0f} ({v2}%)', va='center', alpha=0.9, **font)

ax.set_facecolor('#daedf4')
ax.set_xticklabels([f'{int(x):,}' for x in ax.get_xticks().tolist()])
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(axis='y', left=False, pad=0)

plt.title('Healthcare Expenditures by OECD Countries in 2016', **font, fontsize=20)
plt.xlabel('Expenditures per Capita in USD (% of GDP in Parentheses)', **font, fontsize=15)
plt.xticks(**font, fontsize=12)
plt.yticks(**font, fontsize=12)
plt.margins(x=0.08, y=0.01)
plt.tight_layout()
plt.savefig('Healthcare_Expenditures_by_OECD_Countries_graph.png', ppi=300)
plt.show()
