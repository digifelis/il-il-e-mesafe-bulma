# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 10:56:00 2023

@author: reberezinar
"""
import pandas as pd
df = pd.read_csv(r"titanic.csv", index_col=0)

df.columns
df["Sex"].unique()
erkekler = df[df.Sex == "male" ]

df[df["Age"] > 25]

df[(df.Age > 25) & (df.Sex == "male")]
df.describe()
df.isnull().sum()
df.Age.mean()

df["Age"]= df["Age"].fillna(df.Age.mean())
df.isnull().sum()
# 29.69911764705882
data = df.copy()
data["Sex"][data.Sex == "male"] = 1
data["Sex"][data.Sex == "female"] = 0
data["x"] = 0

'''
cinsiyeti kadın olup yaşı 50'den büyük olanlar 
x kolonunda 1 olarak ifade edilecek

cinsiyeti kadın olup yaşı 50'den küçük olanlar 
x kolonunda 0 olarak ifade edilecek

cinsiyeti erkek olup yaşı 50'den büyük olanlar 
y kolonunda 1 olarak ifade edilecek

cinsiyeti erkek olup yaşı 50'den küçük olanlar 
y kolonunda 0 olarak ifade edilecek

ardından x kolon 1 değer sayısı bulunacak
ardından x kolon 0 değer sayısı bulunacak
ardından y kolon 1 değer sayısı bulunacak
ardından y kolon 0 değer sayısı bulunacak
'''
data["y"] = 0

data["x"][(data.Sex == 0) & (data.Age > 50)] = 1
data["x"][(data.Sex == 0) & (data.Age < 50)] = 0

data["y"][(data.Sex == 1) & (data.Age > 50)] = 1
data["y"][(data.Sex == 1) & (data.Age < 50)] = 0


for index, row in data.iterrows():
    if row.Sex == 0 and row.Age > 50:
        row.x = 1
    if row.Sex == 0 and row.Age < 50:
        row.x = 0
    if row.Sex == 1 and row.Age > 50:
        row.y = 1
    if row.Sex == 1 and row.Age > 50:
        row.y = 0

#data.X = data[(data.Sex == 0) & (data.Age > 50)]















