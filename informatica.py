import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as mpl
from colour import Color

mpl.rcParams['axes.spines.left'] = False
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.bottom'] = True

tab = pd.read_csv('informatica/Video_Games.csv')
tab = pd.DataFrame(tab)



d = tab.groupby(['Platform'])[['Global_Sales']].sum()
d['data'] = d.index
d = d[d['Global_Sales'] > 10]
d = d.sort_values('Global_Sales')

# Critic_Score
f = plt.figure(figsize=(13,10))
f.subplots_adjust(wspace=0.5, hspace=1)

red = list(Color("red").range_to(Color("red"),1))
gray = list(Color("gray").range_to(Color("gray"), 22))
green = list(Color("green").range_to(Color("green"),1))
colors = red + gray + green
colors = [color.rgb for color in colors]

plt.subplot(1,2,1)
plt.barh(d['data'], d['Global_Sales'], color=colors)
plt.title('Vendas por console')
plt.yticks(size=8)

gray = list(Color("red").range_to(Color("green"), 10))
colors = gray
colors = [color.rgb for color in gray]

tab['Critic_Score'] = tab['Critic_Score'].apply(lambda x : float(x))
tab['Name'] = tab['Name'].apply(lambda x : str(x))
tab = tab.sort_values('Critic_Score')
plt.subplot(1,2,2)
plt.barh(tab['Name'][:10], tab['Critic_Score'][:10], color=colors)
plt.title('Jogos mais vendidos')
plt.yticks(size=8)
plt.savefig('informatica/imagem.png')

plt.show()


