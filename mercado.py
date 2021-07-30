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

tab = pd.read_excel('mercado/vodca_price.xlsx')
tab = pd.DataFrame(tab)
tab = tab.sort_values('Psale')
tab_venda = tab[tab['Psale'] != 0]
tab_parado = tab[tab['Psale'] == 0]
tabe = pd.DataFrame({'Situação': ['Vendido', 'Não vendido'],'Quantidade':[len(tab_venda),len(tab_parado)]})

red = list(Color("royalblue").range_to(Color("royalblue"),1))
# cinza = list(Color("grey").range_to(Color("grey"), 7))
green = list(Color("blue").range_to(Color("blue"),1))
colors = red + green
colors = [color.rgb for color in colors]

f = plt.figure(figsize=(13,10))
f.subplots_adjust(wspace=0.5, hspace=1)

plt.subplot(2,2,1)
plt.barh(tabe['Situação'], tabe['Quantidade'], color=colors)
plt.title('Situação (01/2018)')
plt.xticks(rotation=45,ha='right', size=8)
plt.yticks(size=8)

red = list(Color("red").range_to(Color("red"),1))
cinza = list(Color("grey").range_to(Color("grey"), 14))
green = list(Color("green").range_to(Color("green"),1))
colors = red + cinza + green
colors = [color.rgb for color in colors]

plt.subplot(1,2,2)
tab_venda = tab.sort_values('Preço')
plt.barh(tab_venda['Pname'][-16:], tab_venda['Preço'][-16:], color=colors)
plt.yticks(size=5)
plt.title('Produtos mais vendidos')
plt.savefig('mercado/imagem.png')

plt.show()
