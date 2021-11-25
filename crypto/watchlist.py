# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 14:00:53 2021

@author: joanv
"""

from requests import Request, Session
import requests
import time
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'300',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'XXX',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


#page: string of all the content of a page (i.e. https://coinmarketcap.com/currencies/bitcoin/
#finds the watchlist number 
def get_watchlist(page):
    idx = str(page.content).find("watchlists")

    text = str(page.content)[idx-20:idx-1]

    numb = int(text.split(" ")[1].replace(",",""))
    return numb

L = []
S = []
for coin in data["data"]:
    L.append(coin["slug"])
    S.append(coin["symbol"])
   

    
N = []
for i,coin in enumerate(L[:200]):
    if i%5==0:
        time.sleep(5)
    page = requests.get("https://coinmarketcap.com/currencies/{}/".format(coin))
    N.append(get_watchlist(page))
    
    print(coin,get_watchlist(page))
    
    


import pandas as pd
pd.DataFrame((S[:200],L[:200],N),index=["symbol","name","watchlist"]).T.to_csv("C:/Users/joanv/OneDrive/Escritorio/code/crypto/watchlist.txt")
        
        
        

