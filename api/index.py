# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 00:56:47 2023

@author: reberezinar
"""

import mysql.connector
import pandas as pd
import numpy as np

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    sehirAdikaynak: str
    ilceAdiKaynak: str 
    sehirAdiHedef: str
    ilceAdiHedef: str


app = FastAPI()

@app.post("/")
async def create_item(item: Item, q: str):
    result = { **item.dict()}
    if q:
        result.update({"q": q})
    return result

'''
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mesafeler"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM mesafetable1 where sehirAdikaynak = %s and ilceAdiKaynak = %s and sehirAdiHedef = %s and ilceAdiHedef = %s"
params = (sehirAdikaynak,ilceAdiKaynak,sehirAdiHedef,ilceAdiHedef)

mycursor.execute(sql, params)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

'''