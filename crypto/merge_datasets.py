# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 16:22:08 2021

@author: joanv
"""

import pandas as pd

# Create 

#watchlists
df_watchlist = pd.read_csv("C:/Users/joanv/OneDrive/Escritorio/code/crypto/watchlist.txt",index_col=(0))

#get price
price = [data["data"][i]["quote"]["USD"]["price"] for i in range(300)]
market_cap = [data["data"][i]["quote"]["USD"]["market_cap"] for i in range(300)]
symbol = [data["data"][i]["symbol"] for i in range(200)]

df_price = pd.DataFrame((symbol,price,market_cap),index=["symbol","price","market_cap"]).T

df_price_watchlist = df_price.merge(df_watchlist[["symbol","watchlist"]],how="left",on="symbol")

df_price_watchlist.to_csv("C:/Users/joanv/OneDrive/Escritorio/code/crypto/price_watchlist.txt")


df_minmax = pd.read_csv("C:/Users/joanv/OneDrive/Escritorio/code/crypto/min_max_days.txt",index_col=(0))

df_price_watchlist_minmax = df_price_watchlist.merge(df_minmax[["symbol","min_date","max_date","max_price","min_price"]],how="left",on="symbol")


#links
links = ["https://coinmarketcap.com/currencies/{}/".format(df_watchlist.iloc[i,1]) for i in range(len(df_watchlist))]
symbols = [df_watchlist.iloc[i,0] for i in range(len(df_watchlist))]
df_links = pd.DataFrame((symbols,links),index=["symbol","link"]).T

df_price_watchlist_minmax = df_price_watchlist_minmax.merge(df_links[["symbol","link"]],how="left",on="symbol")


df_price_watchlist_minmax.to_csv("C:/Users/joanv/OneDrive/Escritorio/code/crypto/price_watchlist_minmax.txt")







