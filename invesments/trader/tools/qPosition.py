#https://ranaroussi.github.io/yfinance/index.html
import pandas as pd
import datetime
import sys
import json
Print=False
DEBUG=False
WRITTE=False
f_date=datetime.datetime.now().strftime("%Y-%m-%d:%H:%M")
tickersList="Tickers_owned.json"
Data="data.json"
OUTPUTFILE="qPosition.csv"
Direction="Long"

def jSonPrint(Myinfo):
    fData=json.dumps(Myinfo,indent=4)
    print(fData)
    
def divide(x, y):
    return x/y if y else 0


def wLine(row):
    myRow=str(row)
    with open(OUTPUTFILE,'a') as L:
        L.write(myRow)

def Usage():
        print ("Usage : {Ticker} -- Mandatoriey")
        print ("         Arg w   -- Writtes a csv file out")
        quit()

def TradeOff (Trades,ThisDirection,ThisQty,ThisPrice):
        _TradeOff=False
        for Trade in Trades:
            if Trade['On']:
                if ThisDirection != Trade['Direction'] and ThisQty == Trade['Qty']:
                    Trade['On']=False
                    _TradeOff=True
                    break
        if _TradeOff: print("Trade was turned off")
        else:
            print("Not Trade was turned off check Data")
        return(Trades)
                    

#### Computes a Position updating size and Purchase price Average

def cPosition (Ticker,Trades):
    Total=0
    Size=0
    Position={}
    S_Qty=0
    L_Total=0
    L_Qty=0
    L_Commission=0
    S_Total=0
    S_Qty=0
    S_Commission=0
    global DEBUG,WRITTE
    TradesOn=0
    for Trade in Trades:
        
        Direction="Long"
        if Trade['On']:
            TradesOn +=1
            if DEBUG: print("Price=", float(Trade['PriceIn']))
            if DEBUG: print("Qty = ", float(Trade['Qty']))
            if DEBUG: print("Commission = ", float(Trade['Commission']))
            if DEBUG: print("Direction <=>",Trade['Direction'])
            _row=Ticker+","+Trade['Direction']+","+str(Trade['PriceIn'])+","+str(Trade['Qty'])+","+str(Trade['Commission'])+"\n"
            if WRITTE: wLine(_row)
            
            if Trade['Direction']== "Long":
                L_Total=L_Total+float(Trade['PriceIn'])*float(Trade['Qty'])
                L_Commission = L_Commission+float(Trade['Commission'])
                L_Qty=L_Qty+float(Trade['Qty'])
            
            if Trade['Direction'] == "Short":
                S_Total=S_Total+float(Trade['PriceIn'])*float(Trade['Qty'])
                S_Commission = S_Commission+float(Trade['Commission'])
                S_Qty=S_Qty+float(Trade['Qty'])
    
    #AvgPrice=Total/Size ### Replaced for function to fix divide by zero when sales the max
    #number of Stocks owned 
    L_Total=L_Total+L_Commission
    S_Total=S_Total+S_Commission
    if S_Qty > L_Qty:Direction="Short"
    Total=abs(L_Total-S_Total)
    Size=abs(L_Qty-S_Qty)
    AvgPrice=divide(Total,Size)
    if __name__ == "__main__":
        print("Trades On =",TradesOn)
        print("Direction =",Direction)
        print("Total Invested w/comm =",Total)
        print("Current Position size =",Size)
        print("AVG Price =",AvgPrice)
    Myinfo={}
    Myinfo['Ticker']=Ticker
    Myinfo['TradesOn']=TradesOn
    Myinfo['Date']=f_date
    Myinfo['Direction']=Direction
    Myinfo['InvestedAmount']=Total
    Myinfo['PositionSize']=Size
    Myinfo['EntryPrice']=AvgPrice  
    return(Myinfo)
    
    


###Adds a new Trade 
def queryPosition(Ticker):
    ####Defaults for new Trades###
    _On=True
    DateOut=''
    Position={}
    DivAmnt=0
    PriceOut=0
    global WRITTE

    ##Load Data
    df=pd.read_json(Data, orient='index')
    #Validate if Ticker already exist in df
    exist=Ticker in df.index
    if exist:
        Trades=df.loc[Ticker,'Trades']
        if DEBUG:
            print("Existent Trades:")
            print(Trades)

   
        #df.at[Ticker,'Trades']=Trades

        

        DivAmt=float(df.loc[Ticker,'Div'])*float(df.loc[Ticker,'Qty'])
        Myinfo=cPosition(Ticker,Trades)
        Myinfo['Div']=df.loc[Ticker,'Div']
        Myinfo['DivPayOut']=DivAmt
        if __name__ == "__main__":
            print(Ticker,df.loc[Ticker,'Div'],df.loc[Ticker,'Qty'],"DivAmnt =",DivAmt)
            jSonPrint(Myinfo)
        else:
            return json.dumps(Myinfo)
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
    global WRITTE
    import sys
    if len(sys.argv) < 2:
        Usage()
    else:
        Ticker=sys.argv[1]
        if len(sys.argv)>2:
            if sys.argv[2].upper() == "W":
                WRITTE=True
            else:
                Usage()
    print("Ticker : ",Ticker)
    print("File creation :",WRITTE)
    queryPosition(Ticker)
  
####
# MAIN
###      
if __name__ == "__main__":
    main()