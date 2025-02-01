
#https://docs.python.org/3/howto/regex.html#search-and-replace
#This function replaces the old DecPlaces
# it truncates the decimals taking the 'Dec' number as the number of decimal places
#  to return
# Example as a standalone program: 
#python3 decnum.py 9.99999
#                   returns 9.99
#python3 decnum.py 9.99999 3
#                   returns 9.999
#python3 decnum.py 9
#                   returns 9
#
# as a function 
#                decNum(NumbertoTruncate,Numberofdecimalplaces)
#                decNum(9.9999,2) === > 9.99
#                decNum(9.9999,3) === > 9.999
#                decNum(9.9999,0) === > 9.0
#                decNum(9.9999,1) === > 9.9
# Ver 1.0 2025/02/01
import re
import json
DEBUG=False
#
def Usage():
        print ("Usage :   Num  = Number to be truncated -  Mandatory")
        print ("         (Num Dec)= number of decimals to be truncated default 2")
        quit()
def jSonPrint(Myinfo):
    fData=json.dumps(Myinfo,indent=4)
    print(fData)
#
def decNum(Num,Dec):
    Myinfo={}
    pattern="(.*\.\d{0,"+str(Dec)+"})"
    p= re.compile(pattern)
    strValue=str(Num)
    strValueTruncated=p.findall(strValue)
    if strValueTruncated:
        NewNum=float(strValueTruncated[0])
    else:
        NewNum=Num
    Myinfo['NewNum']=NewNum
    if __name__ == "__main__":
        jSonPrint(Myinfo)
    return NewNum
#
def main():
    import sys
    Dec=2
    if len(sys.argv) < 1:
        Usage()
    else:
        if len(sys.argv) == 2:
            decNum(sys.argv[1],Dec)
        else:
            decNum(sys.argv[1],sys.argv[2])
#
if __name__ == "__main__":
    main()