#!/usr/bin/env python3

from fastapi import Request, FastAPI
from typing import Optional
from pydantic import BaseModel
import pandas as pd
import json
import os
import mysql.connector
api = FastAPI()
DBHOST = "ds2022.cqee4iwdcaph.us-east-1.rds.amazonaws.com"
DBUSER = "admin"
DBPASS = os.getenv('DBPASS')
DB = "mjy7nw"
db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB)
cur=db.cursor()

@api.get("/")  # zone apex
def zone_apex():
    return {"Hello": "Hello API"}

@api.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}
@api.get("/customer/{idx}")
def get_customer(idx: int):
    #Read data from csv
    df = pd.read_csv("../customers.csv")
    #Filter based on index
    customer = df.loc[idx]
    return customer.to_dict()
@api.post("/get_payload")
async def get_payload(request: Request):
    response = await request.json()
    geo = response.get("geo")
    url = "https://maps.google.com/?q={geo}".format(geo=geo)
    return {"url": url}
    #return await request.json()
