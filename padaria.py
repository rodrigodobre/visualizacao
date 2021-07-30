import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as mpl
from colour import Color
import datetime as dt
import random
mpl.rcParams['axes.spines.left'] = False
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.bottom'] = True

tab = pd.read_excel('padaria/venda.xlsx')
tab = pd.DataFrame(tab)
b = tab.groupby(['item'])[['diferença']].sum()
b['nome'] = b.index
b = b.sort_values('diferença')

maior = b['nome'][-1]
maior_tab = tab[tab['item'] == maior]
print(maior_tab)
maior_tab = maior_tab.sort_values('data venda')

c = maior_tab.groupby(['hora']).sum()
c['nome'] = c.index

f = plt.figure(figsize=(13,10))
f.subplots_adjust(wspace=0.5, hspace=1)

red = list(Color("red").range_to(Color("red"),1))
cinza = list(Color("grey").range_to(Color("grey"), 4))
green = list(Color("green").range_to(Color("green"),1))
colors = red + cinza + green
colors = [color.rgb for color in colors]

plt.subplot(1,2,2)
plt.barh(b['nome'], b['diferença'], color=colors)
plt.title('Lucro entre 20/05 e 22/05/2020')
plt.xticks(ha='right', size=8)
plt.yticks(size=8)

plt.subplot(1,2,1)
plt.barh(c['nome'], c['diferença'])
plt.title('Venda/hora \nproduto maior lucro')
plt.yticks(list(range(0,25)), labels=[str('%02d') % x   + 'hs' for x in list(range(0,25))], ha='right', size=8)
plt.yticks(size=8)
plt.savefig('padaria/imagem.png')

plt.show()


