DEBUG=True
tickersList="../Tickers_owned.json"
from getAtr import gATR
from getRvol import gRVOL

#


#
#  Main
#
def main():
    import sys
    if len(sys.argv) > 1:
     ARG=sys.argv[1]
     Tickers=ARG.split(",")
     if DEBUG: print("Sent :",Tickers)
    else:
        print("If no ARG working with ",tickersList)
        import json
        with open (tickersList,'r') as f:
            Tickers = json.load(f)
    ATR=gATR(Tickers)
    RVOL=gRVOL(Tickers)
    if DEBUG: print("Received ATR :",ATR)
    if DEBUG: print("Received RVOL :",RVOL)
if __name__ == "__main__":
    main()