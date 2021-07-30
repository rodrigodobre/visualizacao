import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as mpl
from colour import Color

mpl.rcParams['axes.spines.left'] = False
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.bottom'] = True

tab = pd.read_excel('roupa/hering.xlsx')
tab = pd.DataFrame(tab).dropna()
tab['novo'] = tab['precoSemDesconto'] - tab['precoComDesconto']

tab_vend = tab[tab['DisponÃ­vel'] == 'VENDIDO']
tab_nao_vend = tab[tab['DisponÃ­vel'] != 'VENDIDO']

a = tab.groupby(['nomeDaPeca'])[['precoSemDesconto','precoComDesconto']].mean()
a['nome'] = a.index
a['nome'] = a['nome'].apply(lambda x : x.replace('\n', ''))
a['nome'] = a['nome'].apply(lambda x : x.replace('Renner', ''))
a['nome'] = a['nome'].apply(lambda x : x.replace('CalÃ§a', 'Calça'))
a.index = a['nome']
# a = a.sort_values('novo')[-9:]

b = tab_vend.groupby(['Composicao']).count()
b['nome'] = b.index
b = b[b['nome'] != 'Sem etiqueta']
b = b[b['nome'] != 'Sem Etiqueta']
b = b[b['nome'] != 'Indefinida']
b = b[b['nome'] != 'Indefinido']
b = b[b['nome'] != 'sem etiqueta']
b = b[b['nome'] != 'indefinida']
b['nome'] = b['nome'].apply(lambda x : x.replace('algodÃ£o', 'algodão'))
b['nome'] = b['nome'].apply(lambda x : x.replace('ConstruÃ§Ã£o', 'Composição'))
b['nome'] = b['nome'].apply(lambda x : x.replace('AlgodÃ£o', 'algodão'))
b['nome'] = b['nome'].apply(lambda x : x.replace('ComposiÃ§Ã£o', 'Composição'))
b['nome'] = b['nome'].apply(lambda x : x.replace('poliÃ©ster', 'poliéster'))
b.index = list(range(0, len(b)))
b = b.sort_values('novo')[-15:]


print(b['nome'].values)

red = list(Color("red").range_to(Color("red"),1))
cinza = list(Color("grey").range_to(Color("grey"), 13))
green = list(Color("green").range_to(Color("green"),1))
colors = red + cinza + green
colors = [color.rgb for color in colors]

plt.figure(figsize=(13,10))
plt.subplot(2,3,5)
p1 = plt.barh(a['nome'][-9:], a['precoSemDesconto'][-9:], color='royalblue')
p2 = plt.barh(a['nome'][-9:], a['precoComDesconto'][-9:], color='b')
plt.title('Valores com e sem desconto')
plt.xticks(rotation=45,ha='right', size=8)
plt.yticks(size=8)

plt.subplot(2,2,2)
plt.barh(b['nome'], b['marca'], color=colors)
plt.title('Composição mais vendida')
plt.yticks(size=8)
plt.xticks(rotation=45,ha='right', size=8)
plt.savefig('roupa/imagem2.png')

plt.show()
