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

tab = pd.read_excel('distribuidora/ranking.xlsx')
tab = pd.DataFrame(tab)
tab['review_score'] = tab['review_score'].apply(lambda x : int(x))
tab['review_comment_message'] = tab['review_comment_message'].apply(lambda x : str(x))
tab = tab.sort_values('review_score')
tab2 = tab.fillna(0)
tab1 = tab2[tab2['review_comment_title'] != 0]
tab2 = tab1[tab1['review_score'] < 2]
a = tab2.groupby(['review_comment_title']).count()
a['nome'] = a.index
a = a.sort_values('review_id')[-9:]

b = tab1.groupby(['review_score']).count()
b['nome'] = b.index

red = list(Color("red").range_to(Color("red"),1))
cinza = list(Color("grey").range_to(Color("grey"), 7))
green = list(Color("green").range_to(Color("green"),1))
colors = red + cinza + green
colors = [color.rgb for color in colors]

f = plt.figure(figsize=(13,10))
f.subplots_adjust(wspace=0.5, hspace=1)

plt.subplot(1,2,1)
plt.barh(a['nome'][:10],a['review_score'][:10], color=colors)
plt.title('Avaliações')
plt.xticks(rotation=45,ha='right', size=8)
plt.yticks(size=8)

red = list(Color("#000000").range_to(Color("#000000"),1))
cinza = list(Color("grey").range_to(Color("grey"), 3))
green = list(Color("blue").range_to(Color("blue"),1))
colors = red + cinza + green
colors = [color.rgb for color in colors]

plt.subplot(1,2,2)
plt.bar(b['nome'], b['review_id'], color=colors)
plt.title('Contagem ranking')
plt.xticks(ha='right', size=8)
plt.yticks(size=8)
plt.savefig('distribuidora/imagem.png')
plt.show()
