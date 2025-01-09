
#https://www.geeksforgeeks.org/different-ways-to-iterate-over-rows-in-pandas-dataframe/
import datetime
import json
Print=False
OutputFile=False
Period=14
tickersList="../Tickers_owned.json"


def gATR(Tickers):
    print("received ARGS",Tickers)
    for Ticker in Tickers:
        print("->",Ticker)
        import yfinance as yf
        data=yf.download(Ticker)
        df=data.tail(Period+1)
        print(df)
        import pandas as pd
        import numpy as py
        if OutputFile:
            df.to_csv('ATR_tmpout.csv')
        for i in range(len(df)):
            if i == 0:
                print("First Row",df.iloc[i])
                High=float(0)
                Low=float(0)
                pClose=float(0)
                pC=0
            while i > 0:
                
                High=df.iat[i,1]
                Low=df.iat[i,2]
                pC=i-1
                pClose=df.iat[pC,0]
                HLD=High-Low
                HPC=abs(High-pClose)
                LPC=abs(Low-pClose)
                _High=f"{High:.2f}"
                _Low=f"{Low:.2f}"
                _pClose=f"{High:.2f}"
                _HLD=f"{HLD:.2f}"
                _HPC=f"{HPC:.2f}"
                _LPC=f"{LPC:.2f}"
                print("High :",_High,"Low :",_Low,"pClose =",_pClose,"HLD = ",_HLD,"HPC =",_HPC,"LPC = ",_LPC)
                break
                
                
        
    return Tickers
    
    


#
#  Main
#
def main():
    import sys
    if len(sys.argv) > 1:
     ARG=sys.argv[1]
     Tickers=ARG.split(",")
    else:
        print("If no ARG working with ",tickersList)
        with open (tickersList,'r') as f:
            Tickers = json.load(f)
    gATR(Tickers)
if __name__ == "__main__":
    main()