
#https://www.geeksforgeeks.org/different-ways-to-iterate-over-rows-in-pandas-dataframe/
#from getAtr import *
#For now only supports one TIcker at the time.


DEBUG=True
Print=False
OutputFile=False
Period=14
tickersList="../Tickers_owned.json"


def gRVOL(Tickers):
    if DEBUG: print("received ARGS",Tickers)
    for Ticker in Tickers:
        import yfinance as yf
        Myinfo={}
        data = yf.Ticker(Ticker)
        if DEBUG: print("Symbol",data.info['symbol'] )
        Vol=float(data.info['volume'])
        Myinfo['volume']=data.info['volume']
        Avgvol=float(data.info['averageVolume'])
        Myinfo['averageVolume']=data.info['averageVolume']
        Rvol=float(Vol/Avgvol)
        Myinfo['Rvol']=Rvol
        RVOL=f"{Myinfo['Rvol']:.2f}"
        if DEBUG: print ("Rvol = ",RVOL)
        return RVOL

def main():
    import sys
    if len(sys.argv) > 1:
        ARG=sys.argv[1]
        Tickers=ARG.split(",")
        gRVOL(Tickers)

if __name__ == "__main__":
    main()