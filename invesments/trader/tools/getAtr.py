
#https://www.geeksforgeeks.org/different-ways-to-iterate-over-rows-in-pandas-dataframe/
import datetime

Print=False
OutputFile=True
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
                df['HLD']=float(0)
                df['HPC']=float(0)
                df['LPC']=float(0)
            while i > 0:
                
                High=df.iat[i,1]
                Low=df.iat[i,2]
                pC=i-1
                pClose=df.iat[pC,0]
                HLD=High-Low
                df.iat[i,5]=HLD
                HPC=abs(High-pClose)
                df.iat[i,6]=HPC
                LPC=abs(Low-pClose)
                df.iat[i,7]=LPC
                _High=f"{High:.2f}"
                _Low=f"{Low:.2f}"
                _pClose=f"{High:.2f}"
                _HLD=f"{HLD:.2f}"
                _HPC=f"{HPC:.2f}"
                _LPC=f"{LPC:.2f}"
                print("High :",_High,"Low :",_Low,"pClose =",_pClose,"HLD = ",_HLD,"HPC =",_HPC,"LPC = ",_LPC)
                break
        #df.drop([0,1])
        df['tr']=df[['HLD','HPC','LPC']].max(axis=1)
        print("DATA FRAME with NEW COLS")
        print(df)
        fATR=df['tr'].sum()
        ATR=f"{fATR/(len(df)-1):.2f}"
        print("<<<<< ATR >>>>> =",ATR)
                
                
        
    return ATR
    
    


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
        import json
        with open (tickersList,'r') as f:
            Tickers = json.load(f)
    gATR(Tickers)
if __name__ == "__main__":
    main()