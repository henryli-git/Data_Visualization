import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets_376235_731395_Military Expenditure.csv')
df = df[['Name', 'Type', '2018']]
df = df[df['Type'] == 'Country']
df = df.dropna()
df = df.sort_values('2018', ascending=False)
other = {'Name': 'Other', '2018': df['2018'][10:].sum()}
df = df.append(other, ignore_index=True)
df = df.sort_values('2018', ascending=False)
df = df[:11]

data = df['2018']
explode = [0, 0.05, 0, 0, 0, 0, 0, 0, 0, 0, 0]
text_props = {'fontsize': 11, 'color': '#400000', 'alpha': 0.75}
font_dict = {'fontsize': 16, 'color': '#400000'}
colors = ["#6e8988",
          "#93926e",
          "#7b7779",
          "#a4ad94",
          "#8f6f67",
          "#8aa1b7",
          "#768670",
          "#a66b58",
          "#6e97a0",
          "#a6abb5",
          "#b5956b"]


def func(pct):
    absolute = int(pct / 100 * data.sum())
    return f"{pct:.1f}%\n({absolute:,})"


plt.figure(figsize=(16, 9))
plt.rcParams['font.family'] = 'Arial Black'
w, l, p = plt.pie(data, labels=df['Name'], labeldistance=1, rotatelabels=10, colors=colors,
                  startangle=90, autopct=lambda pct: func(pct), pctdistance=0.7, explode=explode,
                  textprops=text_props)

p[3].set_rotation(1)
p[4].set_rotation(15)
p[5].set_rotation(27)
p[6].set_rotation(38.75)
p[7].set_rotation(52)
p[8].set_rotation(51.5)
p[8].set_rotation(65.5)
p[9].set_rotation(73.5)
p[10].set_rotation(83)

plt.title('Percentage of Global Military Spending by Country in 2018\n (Expenditures in USD)', y=1.05,
          fontdict=font_dict)
plt.tight_layout()
plt.savefig('Percentage_of_Global_Military_Spending_by_Country.png', ppi=300)
plt.show()
