# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 01:22:22 2023

@author: reberezinar
"""

import requests
import re

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


kaynakIlce = 'ERUH'
kaynakIl = 'SİİRT'

hedefIlce = 'KOZAN'
hedefIl = 'ADANA'

print(kaynakIl.encode('utf-8'))
print(mesafeBul(kaynakIl.encode('utf-8').decode('latin-1'), kaynakIlce.encode('utf-8').decode('latin-1'), hedefIl.encode('utf-8').decode('latin-1'), hedefIlce.encode('utf-8').decode('latin-1')))


input_string = "SİİRT"
encoded_string = input_string.encode('utf-8').decode('latin-1')

print(encoded_string)



import pandas as pd

iller = pd.read_csv("il.csv", header=None,)
iller.rename(columns = {0: 'plaka', 1:'sehirAdi'}, inplace=True)


ilceler = pd.read_csv("ilce.csv", header=None, index_col=0)
ilceler.rename(columns = {1:'sehirPlaka', 2:'ilceAdi'}, inplace=True)


uzakliktablosu = pd.DataFrame(columns=['sehirAdikaynak', 'ilceAdiKaynak', 'sehirAdiHedef', 'ilceAdiHedef', 'mesafe'])


uzakliktablosu.to_csv('my_dataframe.csv', index=False)

    

                
i = 0
for index, ilceKaynak in ilceler.iloc[:3, :].iterrows():
    for index1, ilceHedef in ilceler.iterrows():
        if uzakliktablosu[
            ((uzakliktablosu.sehirAdikaynak == iller[iller.plaka == ilceHedef.sehirPlaka].sehirAdi.values[0]) & 
            (uzakliktablosu.sehirAdiHedef == iller[iller.plaka == ilceKaynak.sehirPlaka].sehirAdi.values[0]) &
            (uzakliktablosu.ilceAdiKaynak == ilceHedef.ilceAdi) & 
            (uzakliktablosu.ilceAdiHedef == ilceKaynak.ilceAdi))
        ].empty:
            uzakliktablosu.at[i, 'sehirAdikaynak'] = iller[iller.plaka == ilceKaynak.sehirPlaka].sehirAdi.values[0]
            uzakliktablosu.at[i, 'ilceAdiKaynak'] = ilceKaynak.ilceAdi
            uzakliktablosu.at[i, 'sehirAdiHedef'] = iller[iller.plaka == ilceHedef.sehirPlaka].sehirAdi.values[0]
            uzakliktablosu.at[i, 'ilceAdiHedef'] = ilceHedef.ilceAdi
            uzakliktablosu.at[i, 'mesafe'] = 0
        i += 1
uzakliktablosu.to_csv('uzakliktablosu.csv', index=False)
'''
|
((uzakliktablosu.sehirAdikaynak != uzakliktablosu.sehirAdiHedef) &
 (uzakliktablosu.ilceAdiKaynak != uzakliktablosu.ilceAdiHedef))
'''
data = pd.read_csv("uzakliktablosu.csv")


for index, row in data.iloc[:3, :].iterrows():
    cevap = mesafeBul(row.sehirAdikaynak.encode('utf-8').decode('latin-1'), 
                    row.ilceAdiKaynak.encode('utf-8').decode('latin-1'), 
                    row.sehirAdiHedef.encode('utf-8').decode('latin-1'), 
                    row.ilceAdiHedef.encode('utf-8').decode('latin-1'))
    print(cevap, row.sehirAdikaynak)






















