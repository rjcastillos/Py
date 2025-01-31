#!/usr/local/bin/python3.6
#on Mac /usr/local/bin/python3.6
#Or Native /usr/bin/python
##################
#RC Oct 2018
#Program_name: Fib
#
#Usage :   fib
#       Fibonacci Calculator
#       Calculates Retracements and Extensions in UP and DOWN trends
#   https://www.investing.com/tools/fibonacci-calculator
#lastest ver. 1.00
#2025 01 30
#changed to ba a  simpler function accepting 2 params
# 2018 11 29 ver 0.02
#       adapts DecPlaces() from q_buycal_00_08.py
#
#2018 10 26
# 01    Implements simple Up trend Fibonacci:
#       given a Low number (Low=A_) and a high (high=B_) one returns:
#   Fib levels (Fib)
#1) 23.6%
#2) 38.2%
#3) 50%
#4) 61.8%
#5) 65%
#6) 76.4%
###      Formula high-(high-Low)*Fib
#
#
####################
#   Import section #
####################
#Import
import sys
import json
from pprint import pprint
from TradeGoals_9 import *
DEBUG=False
#
#Functions
#
def Usage():
        print ("Usage : {Num A} -- Mandatory")
        print ("        {Num B} -- Mandatory")
        quit()
def DecPlaces(MyP):
        DecIn=str(MyP)
        print("Price str =",DecIn)
        Dec=DecIn.split('.')
        MyNumDec=5
        if int(MyP) > 1000 :
            if len(Dec) ==1:  ## Passeed is 99 therefore  Default to .2f
                print("Price ${} does not contains decimals >> assiging .2f by Default".format(MyP))
            elif len(Dec) ==2:      ## Passed is 99.9 0r more 99.999999
                if len(Dec[1]) < 3 : MyNumDec=2  ## Passed is 99.9 or 99.99 Defaults to .2f
        print("Price ${} will contain {} decimals places".format(MyP,MyNumDec))
        return MyNumDec
FibUP = {
        'aHundred':{"Multiplier":0,"value":0},
        'TwoThreeSix':{"Multiplier":0.236,"value":0},
        'ThreeEightyTwo':{"Multiplier":0.382,"value":0},
        'Fifty':{"Multiplier":0.5,"value":0},
        'SixOneEight':{"Multiplier":0.618,"value":0},
        'GoldenPocket':{"Multiplier":0.65,"value":0},
        'Seven86':{"Multiplier":0.786,"value":0},
        'Zero':{"Multiplier":1,"value":0}
        }
FibDown={}
#    print("Price received =",price)
A_=5755
B_=8506.7
#
#
#   PROGRAM
#
#Analizing sys.argv to set variables according with program's options
#
def FibCalc(_Low,_High):
    A_=_Low
    B_=_High
    Myinfo={}
    if __name__ == "__main__":
        print(f'Fib Retracements upTrend from  ${_Low} to ${_High}')
        print('='*50)
    for k in FibUP.keys():
        # ### high-(high-Low)*Fib
        FibUP[k]["value"]=_High-(_High-_Low)*FibUP[k]["Multiplier"]
        Myinfo[k]=FibUP[k]['value']
        if __name__ == "__main__":
            print(f'{k:>25}{FibUP[k]["value"]:>25.2f}')
    if __name__ == "__main__":
        print('-'*50)
        print (json.dumps(Myinfo,indent=4))
    return json.dumps(Myinfo)

def main():
    if len(sys.argv) < 3:
        Usage()
    else:
        A_=float(sys.argv[1])
        B_=float(sys.argv[2])
        FibCalc(A_,B_)

#
####
# MAIN
###      
if __name__ == "__main__":
    main()
