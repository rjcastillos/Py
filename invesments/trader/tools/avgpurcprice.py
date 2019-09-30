#!/usr/local/bin/python3.6
#on Mac /usr/local/bin/python3.6
#Or Native /usr/bin/python
##################
#RC June 2018
#Program_name: avgpurcprise
#Reads csv files downlaoaded in reports from Nex
#Order the trades by date
#calcuates each trade value in fiat multiplyng units by price per unit
#Considers sells as units in negative (i.e -10 in amount means it was a sell of 10 units)
#At the end calculates : a AVG trade price taking in consideration sales and buys
#and a AVG Purchase Price only with amounts and price (unit price) in buy tradesself.
# There is a discussion wheter the AVG Trade Price is the brake even point but is been investigated when
# there is market volalitlity and sales are lower than buys
#
#   Processing of the input file
#   Expects a csv file with the following fields
#   Currency
#   Description
#   Amount
#   Balance
#   Date
#   Filters:
#   "Exchange" in the Description field
#       Parses the Description field extractring the trade Price in USD
#       "Exchange 0.00215722 BTC for USD @ 6480.0 on Exchange wallet"
# change in the filed order 2018.10.08
#   DESCRIPTION,CURRENCY,AMOUNT,BALANCE,DATE,WALLET
#
#
#Ver.Fork from 01.03
#  2018 06
#Usage : python3 avgpurcprise.py  [DEBUG = -d ]
#
# Needed Libs , Sources and references
#
# https://money.stackexchange.com/questions/84730/how-to-calculate-weighted-average-cost-while-taking-into-account-both-buys-and-s
#
#Ver 02.00
# Does the same as avgpurcprice_v01_03.py
#  Date/time  format:
#   https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
# Changes
#   1) Does not brake on Blanace = 0
#   2) Currency harcoded to analyze and summarize one Currency
#Ver 02.02
#   Add the Arguments -date , -K and -B
#   -date = Indicates when the program finishes processing all the datees previuos to this timestamp
#           in the form of "2018-10-17 14:13:00"
#    Examples:
#               python3 avgpurcprice.py -K=LTC   (process every LTC trade in the input file )
#               python3 avgpurcprice.py -d -K=BTC -B=True (Stops BTC processing in DEBUG mode when Balance = 0)
#               python3 avgpurcprice.py -d -K=ETH -date="2018-02-06 23:59:59" (Start processing every ETH trade in DEBUG mode with DATE/TIME after the given timestamp)
#               python3 avgpurcprice.py -d (process every BTC trade in DEBUG mode after Unix Time starts)
#               python3 avgpurcprice.py (process every BTC trade)
#
#Ver 02.03
#               Adds flexible timestamp convertion -TS=EPOCH or -TS=DDMMYY (as default)
#               changes to localtime the conversion of the EPOCH given
#VEr 02.04
#               Adds -T to include x number of trades beofore quit processing the file
#               Introducing the notion of pairs -K with 'USD' cointained in DESCRIPTION
#               Includes the higher and lower trade prices in the scope of the run give by (-date or -B)
####################
#   Import section #
####################
#Import
import sys
import os
import csv
import operator
from pprint import pprint
import datetime
import time
DEBUG=False
ARGS={'-d':False,'-date':"1970-01-01 23:59:59",'-K':"BTC",'-B':False,'-TS':"DDMMYY",'-T':999999}
Trades=[]
H_Trade=0.0
L_Trade=9999999999.0
SumOfAmouts=0.0
TradeValue=0.0
SumOfTrades=0.0
AVGPricePurchase=0.0
SumOfPurchases=0.0
SumOfCoins=0.0
MyWindowPath="C:/Users/g434646/Documents/Personal/Investment/CryptoCurrencies/"
MyOSPath="/Users/ramon/Documents/DocsandMisc/Investment/Cryptocurrencies/Investment/"
MyFile="2018-07-05-ledger-BTC.csv"
MyIfile=0
MyUntilDate_t='2018-08-07 20:02:00'
# Jan 01 1970. (UTC)

def Usage():
    print ("Usage = ",end="")
    pprint(ARGS)
    quit()
#
#Analizing sys.argv to set variables according with program's options
#
if sys.platform == 'darwin':
    filePath=MyOSPath
    os.chdir(MyOSPath)
else:
    os.chdir(MyWindowPath)
    filePath=MyWindowPath
ls=os.listdir()
n=0
for f in ls:
    if "csv" in f : print("{:d} ==> {}".format(n,f))
    n+=1
MyIfile=input("\nSelect File to Procces = ")
MyFile=ls[int(MyIfile)]
print ("Number selected was ({}) Name : {} on {} ".format(MyIfile,MyFile,filePath))

if len(sys.argv) < 2:
    print ("\nNot given parms running with Default value\n")
else:
    ARGS.update({sys.argv[0]:'ProgName'})
    print("Accepted valid ARGs are = ",ARGS)
#    print("Given ARGS")
    for a in sys.argv:
#        print ("A = ", a)
        p=a.split("=")
        if p[0] not in ARGS:
            print("Invalid argument ",p[0])
            Usage()
        else:
            if p[0] == "-d" :       #This is a Switch or Switches all together
                ARGS.update({'-d':True})
                DEBUG=True
            if p[0] == "-date":
                ARGS.update({'-date':p[1]})
            if p[0] == "-K":
                ARGS.update({'-K':p[1]})
            if p[0] == "-B":
                ARGS.update({'-B':p[1]})
            if p[0] == "-TS":
                ARGS.update({'-TS':p[1]})
            if p[0] == "-T":
                ARGS.update({'-T':p[1]})
print("*** ",sys.argv[0], "Starts **", "\nValues :","\nDebug = " , DEBUG )
print("Values : {-date} , {-K} , {-B}".format(**ARGS))
print ("Given date = ", ARGS['-date'])
if ARGS['-B'] : print ("Processing will stop when Balance = 0")
for k,v in ARGS.items():
    print ("Param {} Value {} ".format(k,v))
print("\n\n")
Trades_= int(ARGS['-T'])
MyTrades = 0
MyUntilDate=datetime.datetime.strptime(ARGS['-date'],"%Y-%m-%d %H:%M:%S")
csvfile=csv.DictReader(open(MyFile))
for L in csvfile :
    if str(L["DESCRIPTION"]).startswith("Exchange") and "USD" in L["DESCRIPTION"] and L["CURRENCY"] == ARGS['-K'] :
        #print(L)
        if ARGS['-TS'] == "DDMMYY" : mydate = datetime.datetime.strptime(L['DATE'],"%d-%m-%y %H:%M:%S")
#        if ARGS['-TS'] == "EPOCH"  : mydate = time.strftime("%d-%m-%y %H:%M:%S", time.gmtime(int(L['DATE'])/1000))
        if ARGS['-TS'] == "EPOCH"  : mydate = datetime.datetime.strptime(time.strftime("%d-%m-%y %H:%M:%S", time.localtime(int(L['DATE'])/1000)),"%d-%m-%y %H:%M:%S")
        if ARGS['-B'] and  L["BALANCE"] == "0": ## for Future testing as of 20181017
            print ("==============================================================")
            print ("Balance 0 found => {},{},{}".format(L['BALANCE'],L['DESCRIPTION'],mydate))
            print ("    <-- Note this trade was not included in the process below -->")
            print ("==============================================================","\n")
            break
#        print ("Trades Processed {} out of {}".format(MyTrades,Trades_))
        if mydate < MyUntilDate or MyTrades == Trades_ :
           break
        else:
#           L['DESCRIPTION'].split()[6] **Assumes price is the 6th element in the DESCRIPTION
            Trades.append({'Description':L['DESCRIPTION'],'price':float(L['DESCRIPTION'].split()[6]),'Amount':float(L['AMOUNT']),'Balance':L['BALANCE'],'Date':mydate})
            MyTrades += 1
Trades.sort(key=operator.itemgetter('Date'))
if DEBUG : pprint(Trades)
print ("Balance,Trade Date,Quantity,Trade Price$,Trade Value$ ,Accu Net$")
for T in Trades:
    if float(T['Amount']) > 0 :                 # Purchase
        if float(T['price']) > H_Trade:
            H_Trade = float(T['price'])
        if float(T['price']) < L_Trade:
            L_Trade = float(T['price'])
    TradeValue=T['Amount']*T['price']
    SumOfTrades=SumOfTrades+TradeValue
    SumOfAmouts=SumOfAmouts+T['Amount']
    if DEBUG:
         print ("Amount {} X Price {} ".format(T['Amount'],T['price']))
         print ("Sum of Trades {} AND Sum of Amounts {}".format(SumOfTrades,SumOfAmouts))
    if SumOfAmouts == 0 :
        AccuNET = 0.0
    else:
        AccuNET = SumOfTrades/SumOfAmouts
    print("{},{},{:.8f},{:.5f},{:.5f},{:.5f}".format(T['Balance'],T['Date'],T['Amount'],T['price'],TradeValue,AccuNET))
    if T['Amount']>0.0 :
        SumOfPurchases = SumOfPurchases + TradeValue
        SumOfCoins = SumOfCoins+T['Amount']
print("\nTotals of Trades")
if SumOfCoins :
    print("================")
    print("Num of Trades =" ,len(Trades))
    print("Traded Coins =", '{:,.8f}'.format(SumOfCoins))
    print("Value in Trades =",'${:,.2f}'.format(SumOfPurchases))
    print("Net Trade Price = ",'${:,.5f}'.format(SumOfTrades/SumOfAmouts))
    print("\nTotals of Purchases")
    print("================")
    print("Coins Inventory before fees=", '{:,.8f}'.format(SumOfAmouts))
    print("Fiat value invested =",'${:,.2f}'.format(SumOfTrades))
    print("AVG Purchase price= ",'${:,.5f}'.format(SumOfPurchases/SumOfCoins))
    print("Run Higher price>>> {:>10} (${:,.5f}) <<< ; Lower Price (${:,.5f})".format("",H_Trade,L_Trade))
else:
    print ("Not purchases were found in this file")
print ("\nEnd processing : {}".format(MyFile))
