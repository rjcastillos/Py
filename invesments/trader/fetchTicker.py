import yfinance as yf
import datetime
import sys
Print=False
if len(sys.argv) > 1:
     Ticker=sys.argv[1]
else:
     print("Please indicate a new Ticker to add")
     quit()
#data = yf.download('OXLC')
#print(data.info)
#for k,v in data.info.items():
#   k,v
data = yf.Ticker(Ticker)
print("Symbol",data.info['symbol'] )
print("currentPrice = ",data.info['currentPrice'])
Vol=float(data.info['volume'])
Avgvol=float(data.info['averageVolume'])
Rvol=float(Vol/Avgvol)
print("exDividendDate = ",data.info['exDividendDate'])
datetime1 = datetime.datetime.fromtimestamp(data.info['exDividendDate'])
print("exDiv from utc = ",datetime1)
print("lastDividendValue = ",data.info['lastDividendValue'])
print("Vol    = ",f"{Vol:>15,.0f}")
print("Avgvol = ",f"{Avgvol:>15,.0f}")
print("Rvol   = ",f"{Rvol:>2,.2f}")
if Print:
    for k,v in data.info.items():
        print("[",k,"]","[",v,"]")