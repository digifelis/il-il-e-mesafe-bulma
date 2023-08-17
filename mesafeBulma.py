# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 01:22:22 2023

@author: reberezinar
"""

import requests
import re
import pandas as pd

def mesafeBul(kaynakIl, kaynakIlce, hedefIl, hedefIlce):
    url = "https://www.illerarasimesafe.com/d_save_temp.php"
    payload='start='+kaynakIlce+'%2C'+kaynakIl+'&end='+hedefIlce+'%2C'+hedefIl+''
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    x = re.search(r'<span id=\"result-distance\">(.*) Km</span>', response.text)
    #print(x.group(1))
    return x.group(1)

'''
kaynakIlce = 'ZARA'
kaynakIl = 'sivas'

hedefIlce = 'çilimli'
hedefIl = 'düzce'

print(mesafeBul(kaynakIl.encode('utf-8').decode('latin-1'), kaynakIlce.encode('utf-8').decode('latin-1'), 
                hedefIl.encode('utf-8').decode('latin-1'), hedefIlce.encode('utf-8').decode('latin-1')
                ))


print(mesafeBul(kaynakIl, kaynakIlce, 
                hedefIl, hedefIlce
                ))

iller = pd.read_csv("il.csv", header=None,)
iller.rename(columns = {0: 'plaka', 1:'sehirAdi'}, inplace=True)


ilceler = pd.read_csv("ilce.csv", header=None, index_col=0)
ilceler.rename(columns = {1:'sehirPlaka', 2:'ilceAdi'}, inplace=True)



uzakliktablosu = pd.DataFrame(columns=['sehirAdikaynak', 'ilceAdiKaynak', 'sehirAdiHedef', 'ilceAdiHedef', 'mesafe'])                
i = 0
for id in range(1,85):
  for index, ilceKaynak in ilceler[ilceler.sehirPlaka == id].iterrows():
      for index1, ilceHedef in ilceler.iterrows():
          if uzakliktablosu[
              (uzakliktablosu.sehirAdikaynak == iller[iller.plaka == ilceHedef.sehirPlaka].sehirAdi.values[0]) & 
              (uzakliktablosu.sehirAdiHedef == iller[iller.plaka == ilceKaynak.sehirPlaka].sehirAdi.values[0]) &
              (uzakliktablosu.ilceAdiKaynak == ilceHedef.ilceAdi) & 
              (uzakliktablosu.ilceAdiHedef == ilceKaynak.ilceAdi)
          ].empty:
              uzakliktablosu.at[i, 'sehirAdikaynak'] = iller[iller.plaka == ilceKaynak.sehirPlaka].sehirAdi.values[0]
              uzakliktablosu.at[i, 'ilceAdiKaynak'] = ilceKaynak.ilceAdi
              uzakliktablosu.at[i, 'sehirAdiHedef'] = iller[iller.plaka == ilceHedef.sehirPlaka].sehirAdi.values[0]
              uzakliktablosu.at[i, 'ilceAdiHedef'] = ilceHedef.ilceAdi
              uzakliktablosu.at[i, 'mesafe'] = 0
          i += 1
  uzakliktablosu.to_csv('uzaklıklar/uzakliktablosu_'+str(id)+'.csv', index=False)
  print(id)

############################################################################
for plaka in range(70,83):
    uzakliktablosu = pd.DataFrame(columns=['sehirAdikaynak', 'ilceAdiKaynak', 'sehirAdiHedef', 'ilceAdiHedef', 'mesafe'])
    i = 0
    for index, ilceKaynak in ilceler[ilceler.sehirPlaka == plaka].iterrows():
        for index1, ilceHedef in ilceler.iterrows():
            if uzakliktablosu[
                (uzakliktablosu.sehirAdikaynak == iller[iller.plaka == ilceHedef.sehirPlaka].sehirAdi.values[0]) & 
                (uzakliktablosu.sehirAdiHedef == iller[iller.plaka == ilceKaynak.sehirPlaka].sehirAdi.values[0]) &
                (uzakliktablosu.ilceAdiKaynak == ilceHedef.ilceAdi) & 
                (uzakliktablosu.ilceAdiHedef == ilceKaynak.ilceAdi)
            ].empty:
                uzakliktablosu.at[i, 'sehirAdikaynak'] = iller[iller.plaka == ilceKaynak.sehirPlaka].sehirAdi.values[0]
                uzakliktablosu.at[i, 'ilceAdiKaynak'] = ilceKaynak.ilceAdi
                uzakliktablosu.at[i, 'sehirAdiHedef'] = iller[iller.plaka == ilceHedef.sehirPlaka].sehirAdi.values[0]
                uzakliktablosu.at[i, 'ilceAdiHedef'] = ilceHedef.ilceAdi
                uzakliktablosu.at[i, 'mesafe'] = 0
            i += 1
    uzakliktablosu.to_csv('uzaklıklar1/uzakliktablosu_'+str(plaka)+'.csv', index=False)
'''
###################################################################################
plaka = 64
#for plaka in range(59,65):
uzakliktablosu = pd.read_csv('uzaklıklar1/uzakliktablosu_'+str(plaka)+'.csv')
for index, row in uzakliktablosu.iloc[:,:].iterrows():
    mesafe = mesafeBul(row.sehirAdikaynak.encode('utf-8').decode('latin-1'), 
           row.ilceAdiKaynak.encode('utf-8').decode('latin-1'), 
           row.sehirAdiHedef.encode('utf-8').decode('latin-1'), 
           row.ilceAdiHedef.encode('utf-8').decode('latin-1')
           )
    #print(row, mesafe)
    uzakliktablosu.at[index, 'mesafe'] = mesafe
print(plaka)
uzakliktablosu.to_csv('uzaklıklar2/uzakliktablosu_'+str(plaka)+'.csv', index=False)           

#uzakliktablosu.to_csv('uzaklıklar2/uzakliktablosu_1.csv', index=False)  





#70-75


59-65
37-40









