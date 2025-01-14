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
        print ("         (Commission = '1 USD' Default)")
        print ("         (Direction = 'Long' Default)")
        print ("         (Strategy = 'SniperNine' Default)")
        print ("         (Timein = 'Now' Default)")
        



#### Computes a Position updating size and Purchase price Average

def cPosition (Trades):
    Total=0
    Size=0
    TradesOn=0
    Position={}
    for Trade in Trades:
	    if Trade['On']:
		    if DEBUG: print("Price=", float(Trade['PriceIn']))
		    if DEBUG: print("Qty = ", float(Trade['Qty']))
		    if DEBUG: print("Commission = ", float(Trade['Commission']))
		    Total=(float(Trade['PriceIn'])*float(Trade['Qty']))+float(Trade['Commission'])+Total
		    Size=float(Trade['Qty'])+Size
		    TradesOn=TradesOn+1
        
    AvgPrice=Total/Size
    if DEBUG: print("Total Invested w/comm =",Total)
    if DEBUG: print("New Position size =",Size)
    if DEBUG: print("AVG Price =",AvgPrice)
    Position={"Direction":"Long","Size":Size,"AvgPrice":AvgPrice}
    if DEBUG: print("Computed Position =",Position)
    return(Position,Total)
    
    


###Adds a new Trade 
def addTrade(Action, Ticker,Price,Qty,Commission,Direction,Strategy,DateIn):
    ####Defaults for new Trades###
    _On=True
    DateOut=''
    Position={}
    DivAmnt=0
    newTrade={"On":_On,
              "Strategy":Strategy,
              "Qty":Qty,
              "Direction":Direction,
              "DateIn":DateIn,
              "PriceIn":Price,
              "Commission":Commission,
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
        #Updating the list of Trades in to the df
        df.at[Ticker,'Trades']=Trades
        Position,Total=cPosition(Trades)
        if DEBUG: print("RECEIVED Position =",Position)
        #Updating the Position list inside a dict in the df
        df.at[Ticker,'Positions']=[Position]
        df.at[Ticker,'Qty']=Position['Size']
        df.at[Ticker,'Invested']=Total
        DivAmt=float(df.loc[Ticker,'Div'])*float(df.loc[Ticker,'Qty'])
        df.at[Ticker,'DivAmnt']=DivAmt
        json_file=df.to_json(orient="index")
        with open ("data.json","w") as o:
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
    Commission=1.00
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
         print("Adding Position ",Action,Ticker,Price,Qty,Commission,Direction,Strategy,DateIn)    
         addTrade(Action,Ticker,Price,Qty,Commission,Direction,Strategy,DateIn)
      
if __name__ == "__main__":
    main()