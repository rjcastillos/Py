import pandas as pd
import numpy as py
import datetime
import sys
import json
myFunctionsPath="/Users/ramon/Documents/DocsandMisc/github/projects/localbranching/Py/invesments/trader/tools"
sys.path.insert(0, myFunctionsPath)
from getAtr import *
from getRvol import *

DEBUG=False
FirstTime=False
Headers="Date,Symbol,RVOL,ATR\n"
f_date=datetime.datetime.now().strftime("%Y-%m-%d:%H")
tickersList="Tickers_owned.json"
if len(sys.argv) > 1:
     ARG=sys.argv[1]
     Tickers=ARG.split(",")
else:
     print("If no ARG working with ",tickersList)
     with open (tickersList,'r') as f:
          Tickers = json.load(f)
     
#data = yf.download('OXLC')
#print(data.info)
#for k,v in data.info.items():
#   k,v


if FirstTime:
    with open("RVOL_log.csv","w") as f_log:
        f_log.write(Headers)
    
df=pd.DataFrame({'Date':[],'Ticker':[],'RVOL':[],'ATR':[]})
for Ticker in Tickers:
     if DEBUG: print ("Sys Arg",Ticker)
     df_date=datetime.datetime.now().strftime("%Y-%m-%d")
     # Calling functions ATR and RVOL
     ATR=gATR(Ticker)
     RVOL=gRVOL(Ticker)
     #Filling up df rows
     f_log_row=df_date+","+Ticker+","+RVOL+","+ATR+"\n"
     if DEBUG: print("row ->",len(df),"[",df_date,",",Ticker,",",RVOL,"",ATR,"]")
     
     with open("RVOL_log.csv","a") as f_log:
               f_log.write(f_log_row)
    
     
     df.loc[len(df)]=[df_date,Ticker,RVOL,ATR]
     
     
o=df_date+"_"+"Tickers_Rvol_data.csv"
print(df)
with open(o,'w') as output:
    df.to_csv(output)
    
     