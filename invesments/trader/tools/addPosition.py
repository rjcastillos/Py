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
Direction="Long"

def Usage():
        print ("Usage : {Action (B)uy/(S)ell Ticker Price} -- Mandatories")
        print ("         (Qty = 11) Default")
        print ("         (Commission = '1 USD' Default)")
        print ("         (Direction = 'Long' Default)")
        print ("         (Strategy = 'SniperNine' Default)")
        print ("         (Timein = 'Now' Default)")
        quit()
        

#### Computes a Position updating size and Purchase price Average

def cPosition (Trades):
    Total=0
    Size=0
    Position={}
    
    for Trade in Trades:
        if Trade['On']:
            if DEBUG: print("Price=", float(Trade['PriceIn']))
            if DEBUG: print("Qty = ", float(Trade['Qty']))
            if DEBUG: print("Commission = ", float(Trade['Commission']))
            if Trade['Direction']== "Long":
                Total=(float(Trade['PriceIn'])*float(Trade['Qty']))+float(Trade['Commission'])+Total
                Size=float(Trade['Qty'])+Size
            if Trade['Direction'] == "Short":
                Total=Total-(float(Trade['PriceOut'])*float(Trade['Qty']))
                Size=Size-float(Trade['Qty'])
                
    
                   
        
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
    PriceOut=0
    newTrade={"On":_On,
              "Strategy":Strategy,
              "Qty":Qty,
              "Direction":Direction,
              "DateIn":DateIn,
              "PriceIn":Price,
              "Commission":Commission,
              "DateOut":DateOut,
              "PriceOut":PriceOut}
    ##Load Data
    df=pd.read_json(Data, orient='index')
    #Validate if Ticker already exist in df
    exist=Ticker in df.index
    if exist:
        Trades=df.loc[Ticker,'Trades']
        if DEBUG:
            print("Existent Trades:")
            print(Trades)
        #Checks if the list is a place holder like in the case 
        #of newobj.py and clears the list to start fresh with this Trade 
        if float(Trades[0]['PriceIn']) == 0 and float(Trades[0]['Qty']) == 0:
            Trades.clear()
        if Direction == "Short":   ##Efectively Price depends on directio could be in or out
            PriceOut = Price
            Price = 0   
        Trades.append(newTrade)
        if DEBUG:
            print("New Trade:")
            print(newTrade)
        #Updating the list of Trades in to the df
        df.at[Ticker,'Trades']=Trades
        Position,Total=cPosition(Trades)
        if DEBUG: print("RECEIVED Position =",Position)
        if DEBUG: print("Entering a new [",Direction,"]Position")
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
    DateIn=f_date
    PriceIn=0
    import sys
    if len(sys.argv) < 4:
        Usage()
    else:
        Action=sys.argv[1].capitalize()
        Ticker=sys.argv[2]
        Price=sys.argv[3]
        Qty = sys.argv[4]
        if Action == "B":
            Action = "Buy"
        if Action == "S":
            Action = "Sale"
        if Action != "Buy" and Action != "Sale":
            Usage()
        if len(sys.argv) > 5 :
            Commission = sys.argv[5]
        else:
            Commission=1.00
        if Action == 'Buy':  Direction="Long"
        if Action == 'Sale': Direction="Short"
        print("Adding Position ",Action,Ticker,Price,Qty,Commission,Direction,Strategy,DateIn)
        addTrade(Action,Ticker,Price,Qty,Commission,Direction,Strategy,DateIn)
####
# MAIN
###      
if __name__ == "__main__":
    main()