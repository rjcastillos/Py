import yfinance as yf
import datetime
import sys
Print=False
if len(sys.argv) > 1:
     ARG=sys.argv[1]
else:
     print("Please indicate a new Ticker to add")
     quit()
#data = yf.download('OXLC')
#print(data.info)
#for k,v in data.info.items():
#   k,v
Tickers=ARG.split(",")
for Ticker in Tickers:
    
    print ("Sys Arg",Ticker)
    

data = yf.Ticker(Ticker)
print("Symbol",data.info['symbol'] )
if Print:
    for k,v in data.info.items():
        print("[",k,"]","[",v,"]")
if data.info.get('currentPrice') == None:
    print ("MISSING currentPrice")
    print ("Consider NAV Price",data.info['navPrice'])
else:
    print("currentPrice = ",data.info['currentPrice'])
Vol=float(data.info['volume'])
Avgvol=float(data.info['averageVolume'])
Rvol=float(Vol/Avgvol)
if data.info.get('exDividendDate') == None:
    print ("MISSING exDividendDate")
    datetime1="None"
else:
    print("exDividendDate = ",data.info['exDividendDate'])
    datetime1 = datetime.datetime.fromtimestamp(data.info['exDividendDate'])
print("exDiv from utc = ",datetime1)
if data.info.get('lastDividendValue') == None:
    print ("MISSING lastDividendValue")
else:
    print("lastDividendValue = ",data.info['lastDividendValue'])
print("Vol    = ",f"{Vol:>15,.0f}")
print("Avgvol = ",f"{Avgvol:>15,.0f}")
print("Rvol   = ",f"{Rvol:>2,.2f}")
