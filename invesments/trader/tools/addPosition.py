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

def Usage():
        print ("Usage : {Action (B)uy/(S)ell Ticker Price} -- Mandatories")
        print ("         (Qty = 11) Default")
        print ("         (Direction = 'Long' Default)")
        print ("         (Strategy = 'SniperNine' Default)")
        print ("         (Timein = 'Now' Default)")
        print ("         (Commision = '1 USD' Default)")



def addTrade(Action, Ticker,Price,Qty,Direction,Strategy,DateIn,Commision):
    ####Defaults for new Trades###
    _On=True
    DateOut=''
    newTrade={"On":_On,
              "Strategy":Strategy,
              "Qty":Qty,
              "Direction":Direction,
              "DateIn":DateIn,
              "PriceIn":Price,
              "Commision":Commision,
              "DateOut":DateOut,
              "PriceOut":""}
    ##Load Data
    df=pd.read_json(Data, orient='index')
    #Validate if Ticker already exist in df
    exist=Ticker in df.index
    if exist:
        Trades=df.loc[Ticker,'Trades']
        if DEBUG:
            print("Existent Trades:")
            print(Trades)
        Trades.append(newTrade)
        if DEBUG:
            print("New Trade:")
            print(newTrade)
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
    if len(sys.argv) < 4:
        Usage()

    else:
         Action=sys.argv[1].capitalize()
         Ticker=sys.argv[2]
         Price=sys.argv[3]
         if len(sys.argv) > 4 : Qty = sys.argv[4]
         if Action == "B":  Action = "Buy"
         if Action == "S": Action = "Sale"
         if Action != "Buy" and Action != "Sale":
             Usage()
         print("Adding Position ",Action,Ticker,Price,Qty,Direction,Strategy,DateIn,Commision)    
         addTrade(Action,Ticker,Price,Qty,Direction,Strategy,DateIn,Commision)
      
if __name__ == "__main__":
    main()