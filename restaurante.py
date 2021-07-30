import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as mpl
from colour import Color
import datetime as dt
import random
import scipy as sp


mpl.rcParams['axes.spines.left'] = False
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.bottom'] = True

item = [['bovino',random.choice(list(range(50,140))),0.3],['suino',random.choice(list(range(30,70))),0.2], 
        ['ave',random.choice(list(range(15,25))),0.25], ['peixe',random.choice(list(range(50,100))),0.15]]

hora = ['18','17','16','15','14','13','12','11','10','09','08','07','06']
mes = ['12','11','10','09','08','07','06','05','04','03','02','01']
dia = ['28','27','24','23','22','21','20','19','18','17','16','15','14','13','12','11','10','09','08','07','06','05','04','03','02','01']
n = 0
dic = {'PRODUTO':[],'CUSTO':[], 'PREÇO':[], 'DATA' : [], 'HORA':[]}
while n < 12034:
    a = random.choice(item)
    pre = a[1]
    cust = pre * a[2]
    h = random.choice(hora)
    d = random.choice(dia)
    m = random.choice(mes)
    dat = dt.datetime.fromisoformat('2020-'+ m + '-' + d + ' ' + h + ':00:00')
    dic['PRODUTO'].append(a[0])
    dic['CUSTO'].append(cust)
    dic['PREÇO'].append(pre)
    dic['DATA'].append(dat)
    dic['HORA'].append(h)
    n = n + 1

tab = pd.DataFrame(dic)

tab.to_excel('restaurante/consumo.xlsx', index=False)
tab = pd.read_excel('restaurante/consumo.xlsx')

tab['diferença'] = tab['PREÇO'] - tab['CUSTO']
tab['DATA'] = tab['DATA'].apply(lambda x : x.date())
tab4 = tab[tab['DATA'] < dt.date(2020,3,30)]
tab4 = tab4.groupby(['DATA'])[['diferença']].sum()
tab4['DATA'] = tab4.index

tab = tab[tab['DATA'] < dt.date(2020,3,30)]
tab = tab.groupby(['DATA', 'PRODUTO']).count()

f =plt.figure(figsize=(13,10))
f.subplots_adjust(wspace=1.5, hspace=1)

plt.subplot(2,1,1)
ave = tab.xs('ave', level=1)
bov = tab.xs('bovino', level=1)
su = tab.xs('suino', level=1)
pe = tab.xs('peixe', level=1)
plt.bar(ave.index, ave['CUSTO'])
plt.bar(bov.index, bov['CUSTO'])
plt.bar(su.index, su['CUSTO'])
plt.bar(pe.index, pe['CUSTO'])
plt.legend(['peixe','ave', 'suino', 'bovino'], bbox_to_anchor=(0.98, 1), loc='upper left')
plt.title('PEDIDOS 1° TRIMESTRE')
plt.xticks(rotation=45,ha='right', size=8)
plt.yticks(size=8)

plt.subplot(2,1,2)
xx = list(range(0, len(tab4['DATA'])))
plt.bar(xx, tab4['diferença'])
datas_l = [tab4['DATA'][x] if x % 2 == 0 else '' for x in range(0, len(tab4['DATA']))]
plt.xticks(xx, labels=datas_l,rotation=45,ha='right', size=8)
p = sp.polyfit(xx, tab4['diferença'], deg=50)
y_ = sp.polyval(p, xx)
plt.plot(xx ,y_, color='black')

plt.title('COMSUMO TOTAL 1° TRIMESTRE')
plt.show()
