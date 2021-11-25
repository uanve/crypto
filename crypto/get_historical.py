# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 09:39:52 2021

@author: joanv
"""
from requests import Request, Session
import time
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import requests

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
  
  
  

df = pd.read_csv("C:/Users/joanv/OneDrive/Escritorio/code/crypto/price_watchlist.txt",index_col=(0))
df.head()


for coin in df["symbol"][:10]:
    print(coin)

page = requests.get()


headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url = "https://finance.yahoo.com/quote/{}-USD/history?period1=1606262400&period2=1637798400&interval=1wk&filter=history&frequency=1wk&includeAdjustedClose=true".format(coin)



for i,coin in enumerate(df["symbol"][10:100]):
    print(coin)
    if i%10==0:
        time.sleep(5)
    url = 'https://query1.finance.yahoo.com/v7/finance/download/{}-USD?period1=1606262400&period2=1637798400&interval=1wk&events=history&includeAdjustedClose=true'.format(coin)
    
    req = requests.get(url,headers=headers, timeout=5)
    if req.status_code==404:
        print("coin {} failed".format(coin))
        pass
    url_content = req.content
    
    file_name = "C:/Users/joanv/OneDrive/Escritorio/code/crypto/historical_data/historical_{}.csv".format(coin)
    
    csv_file = open(file_name, 'wb')
    csv_file.write(url_content)
    csv_file.close()


def get_min_max(coin):
    # coin = "BTC"
    try:
        df = pd.read_csv("C:/Users/joanv/OneDrive/Escritorio/code/crypto/historical_data/historical_{}.csv".format(coin))
    except:
        return pd.NA,pd.NA,pd.NA,pd.NA
    if df.shape == (0, 2):
        return pd.NA,pd.NA,pd.NA,pd.NA
    # df.head()
    
    max(df["High"])
    
    from datetime import datetime
    
    return -(datetime.strptime(df["Date"][df["High"].idxmax()],'%Y-%m-%d')-datetime.now()).days,-(datetime.strptime(df["Date"][df["Low"].idxmin()],'%Y-%m-%d')-datetime.now()).days,max(df["High"]),min(df["Low"])

MAX,MIN = [],[]
max_price,min_price = [],[]
coins = df["symbol"][:100].values
for coin in df["symbol"][:100]:
    MAX.append(get_min_max(coin)[0])
    MIN.append(get_min_max(coin)[1])
    max_price.append(get_min_max(coin)[2])
    min_price.append(get_min_max(coin)[3])
    
pd.DataFrame((coins,MIN,MAX,max_price,min_price),index=["symbol","min_date","max_date","max_price","min_price"]).T.to_csv("C:/Users/joanv/OneDrive/Escritorio/code/crypto/min_max_days.txt")


               
    





