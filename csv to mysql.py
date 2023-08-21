# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 22:11:40 2023

@author: reberezinar
"""

import mysql.connector
import pandas as pd
import numpy as np

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mesafeler"
)

mycursor = mydb.cursor()

for plaka in range(1,82):
    df = pd.read_csv("uzaklıklar2/uzakliktablosu_"+str(plaka)+".csv")
    
    for index, row in df.iterrows():
        try:
            if np.isnan(row['mesafe']):
                row.mesafe = 0
            sql = "INSERT INTO mesafetable1 (sehirAdikaynak,ilceAdiKaynak,sehirAdiHedef,ilceAdiHedef,mesafe) VALUES (%s, %s, %s, %s, %s)"
            val = [
              (row.sehirAdikaynak, row.ilceAdiKaynak, row.sehirAdiHedef, row.ilceAdiHedef, row.mesafe),
            ]
            
            mycursor.executemany(sql, val)
            
            mydb.commit()
        except:
            continue
