import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as mpl
from colour import Color
import datetime as dt

mpl.rcParams['axes.spines.left'] = False
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.bottom'] = True

tab = pd.read_excel('roupa/zara.xlsx')
tab = pd.DataFrame(tab).dropna()

tab_vend = tab[tab['DisponÃ­vel'] == 'VENDIDO']
tab_nao_vend = tab[tab['DisponÃ­vel'] != 'VENDIDO']

tab_vend['Data'] = tab_vend['Data'].apply(lambda x : dt.datetime.fromisoformat(x).replace(minute=0, second=0, microsecond=0) + dt.timedelta(hours=1))

a = tab_vend.groupby(['Data'])[['precoSemDesconto']].sum()
a['nome'] = a.index
a.index = range(0,len(a))

b = tab_vend.groupby(['nomeDaPeca'])[['precoComDesconto']].mean()
b['nome'] = b.index
b['nome'] = b['nome'].apply(lambda x : x.replace('\n', ''))
b['nome'] = b['nome'].apply(lambda x : x.replace('Renner', ''))
b['nome'] = b['nome'].apply(lambda x : x.replace('CalÃ§a', 'Calça'))
b.index = list(range(0, len(b)))
b = b.sort_values('precoComDesconto')[-9:]

f = plt.figure(figsize=(13,10))
f.subplots_adjust(wspace=0.025, hspace=1)
plt.subplot(2,2,2)
plt.plot(a['nome'], a['precoSemDesconto'])
plt.title('Vendas')
plt.xticks(rotation=45,ha='right', size=8)
plt.ylabel('Valor em R$')
plt.yticks(size=8)

red = list(Color("red").range_to(Color("red"),1))
cinza = list(Color("grey").range_to(Color("grey"), 7))
green = list(Color("green").range_to(Color("green"),1))
colors = red + cinza + green
colors = [color.rgb for color in colors]

plt.subplot(2,3,5)
plt.barh(b['nome'], b['precoComDesconto'], color=colors)
plt.title('Produtos mais vendidos')
plt.xticks(rotation=45,ha='right', size=10)
plt.savefig('roupa/imagem3.png')

plt.show()
