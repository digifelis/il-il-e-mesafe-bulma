# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 02:11:03 2023

@author: reberezinar
"""

import pandas as pd

df = pd.read_csv('titanic.csv', index_col=0)

def kategorikYap(df, kolonAdi):
    # verilen kolonu kategorik yapıyor
    dummy_df = pd.get_dummies(df[kolonAdi], prefix=kolonAdi)
    df = pd.concat([df, dummy_df], axis=1)
    return df

#tekli kullanım için
df = kategorikYap(df, 'Sex')

# kolon listesi vererek yapabilmek için
kolonlar = ['Sex', 'Pclass']
for kolon in kolonlar:
    df = kategorikYap(df, kolon)


# dataframe içersinde object olan kolonları kategorik olarak dönüştürüyor.
for i in df.columns.tolist():
    if df[i].dtypes == object:
        dummy_df = pd.get_dummies(df[i], prefix=i)
        df = pd.concat([df, dummy_df], axis=1)