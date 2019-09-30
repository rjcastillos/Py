#!/usr/local/bin/python3.6
#on Mac /usr/local/bin/python3.6
#Or Native /usr/bin/python
##################
#RC June 2018
#Program_name: q_buycal
#
# Given a price , range , steps and value in fiat , calculates exactly how many coins can be bought with
# the same investment throughout the price range
# if not Factor is given the default is "1" , this is a work around when the price is not an integer
# for example to invest $20 in XRP @ $0.5897 you can enter
# >py q_buycal.py -d 5897 6000 10 20 10000
# Price $ 0.5897  buy 33.91555028 coins
# etc...
# Price $ 0.5997  buy 33.35000834 coins
#Ver. 0.05
#  2018 06
# Ver. 06 2018 10
#       Add the fee amount not only the Net of each calculation
#Usage :    python3 q_buycal.py [-d] -start -stop -step -I
#           python3 q_buycal.py -T (Target Price)
#           python3 q_buycal.py -distance [price 1] [price 2]
#           python3 q_buycal.py -P [Investment] [WishedCoins]
#           python3 q_buycal.py -K [Investment] [price]
#           python3 q_buycal.py -M [(+/-)percentage] [price]
#           python3 q_buycal.py -F [Gross_Number] ('nex','nexmm','nexmt','amp','fee') (percentage)
#
# Needed Libs , Sources and references
#
# https://docs.python.org/3.5/index.html
#
#lastest ver. 0.08
#2018 10 30
# 03 Adds the options -T for Target and -distance
#   -T calculates the targets of a given position with % UP for bull market
#   or going long and down for shorting
#
#   -distance calculates the % of increase or decrease between 2 prices
#   same as price range in tradeview
# 04 -Due to the lack of  support of floating in range() this version generates the prices in a while loop instead
#    -Impelements a mask according to the number of decimal places given in the input
#    And dpes not use anymore the -F option
#    - takes the abs() of -step to avoid any issues if a negative number is entered as in the previuos version was supported
#    - Adds the Option -P = Price target to buy with I X number of WishedCoins
#    - Adds the Option -K to return the max number of affordable coins given an investment amount (I) and a Price
#    - Adds the Option -M to calculate a percentage based Market's move of a given price
# 05 - Adds the Option -F to calculates a fee given a number an exchange type of fee and optional a raw percentage
#
# 06 - Adds the fee amount not only the Net
#        example : previuos
#               C:\Users\g434646\Documents\Py>py q_buycal.py -F 38.750 amp
#                                           Gross %38.75 < = > Percentage %
#                                           Net   => 38.65312500
#               : New feautre
#                           Adds Fee = 0.096875
# 07 - Changes MyNumDec=2 in linne 77 from 2 to 5 to support -start with 5 decimals specially valuable for coins over $1
# 08 - Fix a bug on -F when given a Percentage to calculate ex: python3 q_buycal.py -F 6400 0.183 and improves its calculation
#      Considers the 'AMP' internal formatting in the decimal precision where we observed is 2f for Fiat and 5f for Coins
#      where we consider 5f for fiat and 8f for coins
#       Option -F :
#                   python3 q_buycal.py -F 6348.2
#                            process the 'nex' % fee out of 6348.2
#                   python3 q_buycal.py -F 8.60 amp
#                           process the 'amp' % fee out of 8.60 plus the rounding aproximate true fee
#                   python3 q_buycal.py -F 100 '' 10  ++++NOTE the '' is needed as _exchange = Null ++++
#                           Calculates th3 10 % out of 100
#       Forces  MyNumDec = 5 if the price is under 1K
#
####################
#   Import section #
####################
#Import
import sys
from pprint import pprint
from TradeGoals_9 import *
DEBUG=False
ARGS={'-d':False,'-start':0,'-stop':0,'-step':0,'-I':0,'-T':100.75,'-distance':[5,10],'-P':{'I':9.99,'WishedCoins':1.99999999},'-K':{'price':6000,'I':9.99},'-M':{'percentage':3,'price':6000.00},'-F':{'Gross':0.0,'Exchange':'nex','percentage':0.100}}
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
