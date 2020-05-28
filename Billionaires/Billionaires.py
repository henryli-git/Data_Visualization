'''Top 10 Wealthiest People in 2019'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Billionaires.csv')

plt.style.use('Solarize_Light2')
plt.rcParams["font.family"] = "Franklin Gothic Medium"

color = ['#17373C', '#17373C', '#17373C', '#17373C', '#2B6832', '#4F9300', '#A1D700', '#17373C', '#17373C', '#17373C']
x = plt.bar(df['name'][:10], df['net_worth'][:10], width=0.6, color=color, alpha=0.8)

nationality = ['U.S', 'France', 'Mexico', 'Spain']
leg = plt.legend(x, nationality, fontsize=8)

legend_color = ['#17373C', '#2B6832', '#4F9300', '#A1D700']
for i in range(0, 4):
    leg.legendHandles[i].set_color(legend_color[i])
for text in leg.get_texts():
    plt.setp(text, color='#0D1C33')

plt.title('Top 10 Wealthiest People in 2019', color='#0D1C33', fontsize=18)
plt.tick_params(bottom=False)
plt.xticks(rotation=65, va='top', fontsize=8)
plt.yticks(size=8)
plt.ylabel('Net Worth in Billions U.S Dollars', color='#0D1C33', fontsize=12)
plt.tight_layout()
plt.savefig('Billionaires_graph.pdf')
plt.show()
