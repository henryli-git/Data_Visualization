import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('population_by_country_2020.csv')

df = df.sort_values('Net Change', ascending=True)
df = df.nsmallest(columns='Net Change', n=30)
df[['num', '%']] = df['Yearly Change'].str.split('%', expand=True)
df['num'] = df['num'].astype(float)

plt.style.use('dark_background')
plt.rcParams["font.family"] = " Lucida Sans Unicode"
fig, ax = plt.subplots(figsize=(16, 9))
colors = [
    "#680002",
    "#8a0003",
    "#940003",
    "#b00004",
    "#cb0004",
    "#e70005",
    "#ff040a",
    "#ff2025",
    "#ff3c40",
    "#ff0c12",
    "#ff1a1f",
    "#ff272c",
    "#ff4246",
    "#ff5d61",
    "#ff787b",
    '#ff9395',
    '#ffbcbd',
    "#ffc9ca",
    "#ffd7d7",
    "#fff2f2",
    "#fff2f2",
    "#fff2f2"
]
plt.bar(x=df['Country (or dependency)'], height=df['Net Change'], width=0.5, align='center', color=colors)
for i, v in enumerate(df['Net Change']):
    plt.text(i, v, "{:,}".format(v), va='top', ha='center', rotation=22, fontsize=9)

plt.title('All Countries with Decreasing Populations in 2020', fontsize=18)
ax.xaxis.tick_top()
plt.xticks(rotation=65, ha='left', fontsize=12)
plt.ylabel('Change in Number of People', fontsize=14)
plt.yticks(fontsize=12)
ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])
plt.tight_layout()
plt.savefig('All_Countries_with_Decreasing_Populations_in_2020_graph', ppi=600)
plt.show()
