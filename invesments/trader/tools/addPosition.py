#https://ranaroussi.github.io/yfinance/index.html
import pandas as pd
import datetime
import sys
import json
Print=False
DEBUG=True
f_date=datetime.datetime.now().strftime("%Y-%m-%d:%H:%M")
tickersList="Tickers_owned.json"
Data="data.json"




def addTrade(Ticker,Price,Qty,Direction,Strategy,DateIn,Commision):
    ####Defaults for new Trades###
    _On=True
    DateOut=''
    PriceOut=''
    newTrade={"On":_On,
          "Strategy":Strategy,
          "Qty":Qty,
          "Direction":Direction,
          "DateIn":DateIn,
          "PriceIn":Price,
          "Commision":Commision,
          "DateOut":DateOut,
          "PriceOut":PriceOut}
    ##Load Data
    df=pd.read_json(Data, orient='index')
    #Validate if Ticker already exist in df
    exist=Ticker in df.index
    if exist:
        Trades=df.loc[Ticker,'Trades']
        Trades.append(newTrade)
        df.at[Ticker,'Trades']=Trades
        json_file=df.to_json(orient="index")
        with open ("new_data.json","w") as o:
             o.write(json_file)      
    else:
        print("Ticker :", Ticker , "Doesn't exist run new object first")
        print("        ","python3 newobj.py <Ticker>")
        

#
#   MAIN
#
def main():
    ####Defaults for new Trades###
    
    Strategy="SniperNine"
    Qty=11
    Direction="Long"
    DateIn=f_date
    PriceIn=0
    Commision=1.00
    import sys
    if len(sys.argv) < 3:
        print ("Usage : {Ticker Price} -- Mandatories")
        print ("         (Qty = 11) Default")
        print ("         (Direction = 'Long' Default)")
        print ("         (Strategy = 'SniperNine' Default)")
        print ("         (Timein = 'Now' Default)")
        print ("         (Commision = '1 USD' Default)")
    else:
         Ticker=sys.argv[1]
         Price=sys.argv[2]
         if len(sys.argv) > 3 : Qty = sys.argv[3]
         addTrade(Ticker,Price,Qty,Direction,Strategy,DateIn,Commision)
      
if __name__ == "__main__":
    main()