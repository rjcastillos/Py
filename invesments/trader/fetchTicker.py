import yfinance as yf
import datetime
import sys
import json
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
     Myinfo={}
     Myinfo['symbol']=data.info['symbol']
     print("Symbol", Myinfo['symbol'])
     #print("currentPrice = ",data.info['currentPrice'])
     if data.info.get('currentPrice') == None:
          print ("taking net asset value nav instead of price")
          Myinfo['currentPrice']=data.info['navPrice']
     else:
          Myinfo['currentPrice']=data.info['currentPrice']
     #print("currentPrice = ",Myinfo['currentPrice'])
     Vol=float(data.info['volume'])
     Myinfo['volume']=data.info['volume']
     Avgvol=float(data.info['averageVolume'])
     Myinfo['averageVolume']=data.info['averageVolume']
     Rvol=float(Vol/Avgvol)
     Myinfo['Rvol']=Rvol
     Myinfo['exDividendDate']=data.info['exDividendDate']
     #print("exDividendDate = ",Myinfo['exDividendDate'])
     datetime1 = datetime.datetime.fromtimestamp(data.info['exDividendDate'])
     Myinfo['exDivFormatted']=datetime1.strftime("%m/%d/%Y")
     #print("exDiv from utc = ",Myinfo['exDivFormatted'])
     Myinfo['lastDividendValue']=data.info['lastDividendValue']
     #print("lastDividendValue = ",Myinfo['lastDividendValue'])
     #print("Vol    = ",f"{Vol:>15,.0f}")
     #print("Avgvol = ",f"{Avgvol:>15,.0f}")
     #print("Rvol   = ",f"{Rvol:>2,.2f}")
     # print(type(Myinfo))
     fData=json.dumps(Myinfo,indent=4)
     print(fData)
if Print:
    for k,v in data.info.items():
        print("[",k,"]","[",v,"]")