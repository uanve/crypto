  
  
import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt
  
def to_float(i):
    i = i[1:]
    i = i.replace(",", "")
    return float(i)

def to_df(file):

    L = []
    f = open(file,"r")
    for e in f:
        e = e[:-1]
        l = e.split("\t")
        
        L.append(np.array(l))
            
    f.close()
    
    df = pd.DataFrame(np.array(L))

    
    for idx in range(1,df.shape[1]):
        df[idx] = df[idx].apply(to_float)
        df[idx] = df[idx].loc[::-1].reset_index(drop=True)
        
    df.rename(columns={0: 'date', 1: "open", 2: "high", 3: "low", 4: "close", 5: "volume", 6: "mark_cap"}, inplace=True)
    return df

last = 150

df = to_df("C:/Users/joanv/OneDrive/Escritorio/test.txt")
df_b = to_df("C:/Users/joanv/OneDrive/Escritorio/bitcoin_year.txt").iloc[last:,:]
df_omg = to_df("C:/Users/joanv/OneDrive/Escritorio/omg_year.txt").iloc[last:,:]

def normal(vect):
    return (vect-min(vect))/(max(vect)-min(vect))

normal(df_b["high"]).plot()
normal(df_omg["high"]).plot()

df_b["high"].plot()
df_omg["high"].plot()



df_omg["high"].plot()


x = sample(-100:100, 50)
normalized = (x-min(x))/(max(x)-min(x))



