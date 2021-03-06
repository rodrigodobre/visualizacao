import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as mpl
from colour import Color

mpl.rcParams['axes.spines.left'] = False
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.bottom'] = True

tab = pd.read_excel('roupa/renner.xlsx')
tab = pd.DataFrame(tab).dropna()
tab_vend = tab[tab['DisponÃ­vel'] == 'VENDIDO']
tab_nao_vend = tab[tab['DisponÃ­vel'] != 'VENDIDO']

a = tab_vend.groupby(['nomeDaPeca'])[['precoSemDesconto']].sum()
a['nome'] = a.index
a['nome'] = a['nome'].apply(lambda x : x.replace('\n', ''))
a['nome'] = a['nome'].apply(lambda x : x.replace('Renner', ''))
a['nome'] = a['nome'].apply(lambda x : x.replace('CalÃ§a', 'Calça'))
a.index = list(range(0, len(a)))
a = a.sort_values('precoSemDesconto')[-9:]

b = tab_vend.groupby(['Cores']).count()
b['nome'] = b.index
b.index = list(range(0, len(b)))
b = b.sort_values('precoSemDesconto')[-5:]

red = list(Color("#e74c3c").range_to(Color("#e74c3c"),1))
cinza = list(Color("#bdc3c7").range_to(Color("#bdc3c7"), 7))
green = list(Color("#27ae60").range_to(Color("#27ae60"),1))
colors = red + cinza + green
colors = [color.rgb for color in colors]

f = plt.figure(figsize=(15,15))
f.subplots_adjust(wspace=0.05, hspace=1)

plt.subplot(2,2,1)
plt.barh(a['nome'], a['precoSemDesconto'], color=colors)
plt.title('Produtos mais vendidos')
plt.xticks(rotation=45,ha='right', size=8)
plt.yticks(size=8)

orange = list(Color("#f39c12").range_to(Color("#f39c12"),1))
red = list(Color("#e74c3c").range_to(Color("#e74c3c"),1))
cinza = list(Color("#bdc3c7").range_to(Color("#bdc3c7"), 1))
black = list(Color("#2c3e50").range_to(Color("#2c3e50"),1))
blue = list(Color("#2980b9").range_to(Color("#2980b9"),1))
colors = orange + red + cinza + black + blue
colors = [color.rgb for color in colors]

plt.subplot(1,2,2)
plt.bar(b['nome'], b['marca'], color=colors)
plt.title('Cores que são mais vendidas')
plt.xticks(rotation=45,ha='right', size=8)
plt.yticks(size=8)
plt.xticks(['','','','',''])
plt.savefig('roupa/imagem1.png')

plt.show()
