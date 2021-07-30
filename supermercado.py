import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as mpl
from colour import Color
import datetime as dt
import scipy as sp

mpl.rcParams['axes.spines.left'] = False
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.bottom'] = True

tab = pd.read_excel('supermercado/super.xlsx')
tab = pd.DataFrame(tab)
tab = tab.replace(['SWEETS','VEGETABLES','SPICES','DRINK_JUICE','ART._HYGIENIC','MEAT','BEER'],
                   ['DOCES', 'VEGETAIS', 'TEMPEROS', 'DRINKS E SUCOS', 'HIGIENE', 'CARNE', 'CERVEJA'])

a = tab.groupby(['Date'])[['quantidade']].sum()
a['data'] = a.index
b = tab.groupby(['Pgroup'])[['quantidade']].count()
b['data'] = b.index
b = b.sort_values('quantidade')

f =plt.figure(figsize=(13,10))
f.subplots_adjust(wspace=0.5, hspace=1)

plt.subplot(2,1,1)
xx = list(range(0, len(a['data'])))
plt.bar(xx, a['quantidade'], alpha=0.5)
# datas_l = [a['data'][x] if x % 2 == 0 else '' for x in range(0, len(a['data']))]
plt.xticks(xx, labels=a['data'],rotation=45,ha='right', size=8)
p = sp.polyfit(xx, a['quantidade'], deg=50)
y_ = sp.polyval(p, xx)
plt.plot(xx ,y_, color='black')
plt.title('ITENS VENDIDOS')

red = list(Color("red").range_to(Color("red"),1))
cinza = list(Color("grey").range_to(Color("grey"), 5))
green = list(Color("green").range_to(Color("green"),1))
colors = red + cinza + green
colors = [color.rgb for color in colors]

plt.subplot(2,2,4)
plt.barh(b['data'], b['quantidade'], color=colors)
plt.title('TOTAL VENDIDOS')
plt.savefig('supermercado/imagem.png')

plt.show()
