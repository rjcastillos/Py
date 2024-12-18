#!/usr/local/bin/python3.6
#on Mac /usr/local/bin/python3.6
#On Windows:
#C:\Users\rcastillo\AppData\Local\Programs\Python\Python39\python.exe q_divcal.py
#Or Native /usr/bin/python
##################
#RC Dec 2024
#Program_name: q_devcal
#
# Calculates the Yearly Dividend Pay off and  the Trailing Annual Dividend Yield of a share
# as well as showing how many shares to get $100 , $50 or $20 every dividend payment date.
# 
# Div = is the payment per share 
# Qty = Owned or estimatated quantinty of shares to purchase
# Price = Share price
# Periodicity = How often the share pays dividends 
#Yearly 
#Bimonthly 
#Quarterly 
#Monthly
# 
# For example  the Ex.  Date of stock "O" is every month , paying $0.2630 per share and the 
# purchase price is $50 
# >python3 q_divcal.py -div 
# 
# 
# 
#Ver. 0.01
#  2024 12 
# Ver. 
#       
#Usage :    python3 q_divcal.py 
#           python3 q_divcal.py 
#           python3 q_divcal.py
#           python3 q_divcal.py 
#           python3 q_divcal.py 
#           python3 q_divcal.py 
#           python3 q_divcal.py 
#
# Needed Libs , Sources and references
#
# https://docs.python.org/3.5/index.html
#
#Latest ver 0.0.1
#2024 12 16
#Improvements made using git in a multi devs enviroment using local dev and features to be pushed to github
#ver. 0.08
#2018 10 30
#
#
####################
#   Import section #
####################
#Import
import sys
from pprint import pprint
from TradeGoals_9 import *
DEBUG=False
ARGS={'-d':False,'-start':0,'-stop':0,'-step':0,'-I':0,'-T':100.75,'-distance':[5,10],'-P':{'I':9.99,'WishedCoins':1.99999999},'-K':{'price':6000,'I':9.99},'-M':{'percentage':3,'price':6000.00},'-F':{'Gross':0.0,'Exchange':'nex','percentage':0.100},'-div':{'Div':1.0,'Price':1.0,'Qty':1.0,'Periodicity':'Y'}}

#
#Functions
#
def Usage():
    print ("Usage = ",end="")
    pprint(ARGS)
    quit()
def DecPlaces(MyP):
        DecIn=str(MyP)
        print("Price str =",DecIn)
        Dec=DecIn.split('.')
        MyNumDec=5
        if int(MyP) > 1000 :
            if len(Dec) ==1:  ## Passeed is 99 therefore  Default to .2f
                print("Price ${} does not contains decimals >> assiging .2f by Default".format(price))
            elif len(Dec) ==2:      ## Passed is 99.9 0r more 99.999999
                if len(Dec[1]) < 3 : MyNumDec=2  ## Passed is 99.9 or 99.99 Defaults to .2f
        print("Price ${} will contain {} decimals places".format(MyP,MyNumDec))
        return MyNumDec
#
#
#   PROGRAM
#
#Analizing sys.argv to set variables according with program's options
#
if len(sys.argv) < 2:
    print ("\nNot given parms running with Default value\n")
else:
    ARGS.update({sys.argv[0]:'ProgName'})
#    print("Accepted valid ARGs are = ",ARGS)
#    print("Given ARGS")
    for a in sys.argv:
#        print ("A = ", a)
        p=a.split("=")
        if p[0] not in ARGS:
            print("Invalid argument ",p[0])
            Usage()
        if len(p) > 1:              #This is a parameter (foo="something")
            ARGS.update({p[0]:float(p[1])})
#            print ("for {} new value = {}".format(*p))
        else:
            if p[0] == "-d" :       #This is a Switch or Switches all together
                ARGS.update({'-d':True})
                DEBUG=True
#                print ("for -d new value = {-d}".format(**ARGS))
            if p[0] == "-T" :
                 Goals(sys.argv[2])
                 quit()
            if p[0] == "-distance" :
                print ("${} < = > ${}".format(sys.argv[2],sys.argv[3]))
                print("Distance % => {:.3f} ".format(Distance(float(sys.argv[2]),float(sys.argv[3]))))
                quit()
######
#
#   Code for Dividends
#
            if p[0] == "-div" :
                Period_Multiplier = {"Y":1.0,"Q":4.0,"B":2.0,"M":12.0}
                Examples=25,50,100
                yearlyDivPayOff =  1.0
                OnePayPercentage = 1.0
                MyDiv = ARGS['-div']
                #print ("Len = ",len(sys.argv))
                #print ("Argv 0",sys.argv[0])
                #print ("Argv 1",sys.argv[1])
                #print ("-div=",ARGS['-div'])
                #print (MyDiv)
                #Div = MyDiv['Div']
                #Price = MyDiv['Price']
                #Qty = MyDiv['Qty']
                #Periodicity = MyDiv['Periodicity']
                if len(sys.argv) > 2:
                    for v in range(2, len(sys.argv)):
                        item,value=sys.argv[v].split("=")
                        value = value.replace(',','.')
                        MyDiv[item]=value
                print ("Dividends Div =",MyDiv['Div'])
                print ("Price =",MyDiv['Price'])
                print ("Periodicity =",MyDiv['Periodicity'])
                print ("Qty =",MyDiv['Qty'])
                print ("End Div Cal")
                Div = float(MyDiv['Div'])
                Price = float(MyDiv['Price'])
                Qty = int(MyDiv['Qty'])
                Periodicity = MyDiv['Periodicity']
#
#               CALCULATIONS
#
                PeriodicityMultiplier=int(Period_Multiplier[Periodicity])
                yearlyDivPayOff = Qty*Div*PeriodicityMultiplier
                yearYield = (yearlyDivPayOff / (Qty*Price))*100
                OnePayment = Qty*Div
                OnePayPercentage = (OnePayment / (Qty * Price))*100
 #
 #              PRINT OUT
 #
                print ("yearlyDivPayOff = ",yearlyDivPayOff )
                print ("yearYield = ",f"{yearYield:.2f}","%" )
                print ("OnePayment = ",f"{OnePayment:.2f}","$")
                print ("OnePayPercentage =",f"{OnePayPercentage:.2f}","%")
                print ("Investment w/o commision =",f"{Qty*Price:.2f}","$")
                print ("Dividend recomendations")
                print ("************************")
                for x in Examples:
                    print ("$",x,"=>",f"{x/Div:.2f}"," shares","Investment =",f"{x/Div*Price:.2f}","$")
#
#              END DIV CAL
#                                 
                quit()
            if p[0] == "-P" :
                print ("Investment ${} < = > Wish Coins {}".format(sys.argv[2],sys.argv[3]))
                nex,amp=MinPrice(sys.argv[2],sys.argv[3])
                print("Nex Price => ${:,.5f}".format(nex['price']))
                print("Amp Price => ${:,.5f}".format(amp['price']))
                quit()
            if p[0] == "-K" :
                print ("Investment ${} < = > Price ${}".format(sys.argv[2],sys.argv[3]))
                print("Affordable Quantity of Coins  => {:,.8f}".format(aCoins(sys.argv[2],sys.argv[3])))
                quit()
            if p[0] == "-M" :
                print ("Move in %{} < = > Price ${}".format(sys.argv[2],sys.argv[3]))
                print("Market move new price  => {:,.5f}".format(float(mMove(sys.argv[2],sys.argv[3]))))
                quit()
            if p[0] == "-F" :
                _gross = float(sys.argv[2])
                _percentage = ''
                _exchange = ''
                print("Length = ",len(sys.argv))
                if len(sys.argv) == 4 :
                    if sys.argv[3] :
                        _exchange = sys.argv[3]
                    else:
                        _exchange = ''
                if len(sys.argv) == 5 :
                    if sys.argv[4] :
                        _percentage = float(sys.argv[4])
                print ("Gross %{} < = > Percentage % {} Exchange : {} ".format(_gross,_percentage,_exchange))
                _Net,_Fee = aFterFee(_gross,_exchange,_percentage)
                print ("Net === > {:.8f} ".format(_Net))
                print ("Fee === > {:.8f}".format(_Fee))
                if _exchange == 'amp':
                    print ("Precision Fee if K === >> {:.5f}".format(_Fee))
                    print ("Precision Fee if Fiat  === >> {:.2f}".format(_Fee))
                quit()
print("*** ",sys.argv[0], "Starts **")
NumDec=DecPlaces(ARGS['-start'])
print("Values : {-start} , {-stop} , {-step}".format(**ARGS))
for k,v in ARGS.items():
    print ("Param {} Value {} ".format(k,v))
print("\n\n")
_start=float(ARGS['-start'])
_stop=float(ARGS['-stop'])
_step=abs(ARGS['-step'])
_I=float(ARGS['-I'])
p=_start
if p < _stop:
    while p < _stop:
        coins = _I/p
        print("Price $ {0:.{1}f}  buy {2:,.8f} coins ".format(p,NumDec,coins))
        p+=_step
else:
    while p > _stop:
        coins = _I/p
        print("Price $ {0:.{1}f}  buy {2:,.8f} coins ".format(p,NumDec,coins))
        p-=_step
