import yfinance as yf
import datetime
Print=False
#data = yf.download('OXLC')
#print(data.info)
#for k,v in data.info.items():
#   k,v
data = yf.Ticker('OXLC')
print("Symbol",data.info['symbol'] )
print("currentPrice = ",data.info['currentPrice'])
Vol=float(data.info['volume'])
Avgvol=float(data.info['averageVolume'])
Rvol=float(Vol/Avgvol)
print("exDividendDate = ",data.info['exDividendDate'])
datetime1 = datetime.datetime.fromtimestamp(data.info['exDividendDate'])
print("exDiv from utc = ",datetime1)
print("lastDividendValue = ",data.info['lastDividendValue'])
print("Vol = ",Vol)
print("Avgvol = ",Avgvol)
print("Rvol = ",Rvol)
if Print:
    for k,v in data.info.items():
        print("[",k,"]","[",v,"]")