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
#lastest ver. 0.01
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
# 2018 11 29 ver 0.02
#       adapts DecPlaces() from q_buycal_00_08.py
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
ARGS={'-A':0.1,'-B':100.00,'-C':0.0,'-F':0.382}
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
FibUP={'TwoThreeSix':0.236,'ThreeEightyTwo':0.382,'Fifty':0.5,'SixOneEight':0.618,'GoldenPocket':0.65,'Seven86':0.786}
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
print("*** ",sys.argv[0], "Starts **")
NumDec=DecPlaces(ARGS['-A'])
print("Values : Low: {-A} , High {-B} , Custom {-C} , Fib {-F} ".format(**ARGS))
for k,v in ARGS.items():
    print ("Param {} Value {} ".format(k,v))
print("\n\n")
A_=float(ARGS['-A'])
B_=float(ARGS['-B'])
C_=float(ARGS['-B'])
#_step=abs(ARGS['-step'])
F_=float(ARGS['-F'])
#
#
print("\nFib Retracements UPTrend from  ${0:,.{1}f} to  ${2:,.{1}f} ".format(A_,NumDec,B_))
print("========================================================","\n")
print("{0:20s}  Fib Up =    ${1:>20,.{2}f}".format("aHundred",B_,NumDec))
for k,v in FibUP.items():
    print("{0:20s}  Fib Up =    ${1:>20,.{2}f}".format(k,B_-(B_-A_)*v,NumDec)) ### high-(high-Low)*Fib
print("{0:20s}  Fib Up =    ${1:>20,.{2}f}".format("Zero",A_,NumDec))
