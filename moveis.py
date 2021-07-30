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

hora = ['18','17','16','15','14','13','12','11','10','09','08','07','06']
mes = ['12','11','10','09','08','07','06','05','04','03','02','01']
dia = ['28','27','24','23','22','21','20','19','18','17','16','15','14','13','12','11','10','09','08','07','06','05','04','03','02','01']

item = ['Acessórios' 'Móveis e Estofados', 'Armário' 'Bancos', 'Banheiros', 'Banqueta', 'Cozinhas', 'Decoração', 'Dormitório Infantil e Bebê', 'Dormitórios e Quartos', 'Lavanderia', 'Mesa de Canto Móveis de Escritório', 'Móveis de Jardim', 'Nicho Sala de Estar', 'Sala de Jantar']
dic = {'item':[],'quant':[], 'data' : []}
n=0
while n < 3002:
    h = random.choice(hora)
    d = random.choice(dia)
    m = random.choice(mes)
    dic['item'].append(random.choice(item))
    dic['quant'].append(random.choice([0,1,3]))
    dic['data'].append(dt.datetime.fromisoformat('2020-'+ m + '-' + d + ' ' + h + ':00:00').date())
    n = n + 1

tab = pd.DataFrame(dic)
tab.to_excel('moveis/moveis.xlsx', index=False)
print(tab)

tab['data_escrita'] = tab['data'].apply(lambda x : x.strftime("%B"))
tab['mes'] = tab['data'].apply(lambda x : x.month)
tab['data_escrita'] = tab['data_escrita'].replace(['November', 'May', 'March', 'April', 'August', 'January' ,'December' ,'July',
'February', 'September', 'June', 'October'], ['Novembro', 'Maio', 'Março', 'Abril', 'Agosto', 'Janeiro', 'Dezembro', 'Julho',
'Fevereiro', 'Setembro', 'Junho', 'Outubro'])

c = tab.groupby(['mes'])[['quant']].sum()
c['data'] = c.index
c['data_esc'] = c['data'].apply(lambda x : dt.date(1,x,1).strftime("%B"))
c['data_esc'] = c['data_esc'].replace(['November', 'May', 'March', 'April', 'August', 'January' ,'December' ,'July',
'February', 'September', 'June', 'October'], ['Novembro', 'Maio', 'Março', 'Abril', 'Agosto', 'Janeiro', 'Dezembro', 'Julho',
'Fevereiro', 'Setembro', 'Junho', 'Outubro'])


d = tab.groupby(['item'])[['quant']].sum()
d['data'] = d.index
d = d.sort_values('quant')
print(d)

f = plt.figure(figsize=(13,10))
f.subplots_adjust(wspace=0.5, hspace=1)

red = list(Color("red").range_to(Color("red"),1))
green = list(Color("green").range_to(Color("green"),1))
colors = red + green
colors = [color.rgb for color in colors]

plt.subplot(1,2,1)
plt.bar([d['data'][0],d['data'][-1]], [d['quant'][0],d['quant'][-1]], color=colors)
plt.title('Item menos\ne\nmais vendido')
plt.yticks(size=8)

colors = list(Color("red").range_to(Color("green"), 13))
colors = [color.rgb for color in colors]

plt.subplot(1,2,2)
plt.barh(c['data'], c['quant'], color=colors)
plt.yticks(c['data'],labels=c['data_esc'],ha='right', size=8)
plt.title('Itens vendidos')
plt.yticks(size=8)
plt.savefig('moveis/imagem.png')

plt.show()


