import json

DEBUG=False
#
# Updates in INPUTFILE
#
INPUTFILE="../update_data.json"
#
#IF NEWFILE <> FILETOUPDATE this will contain only the last update 
#
FILETOUPADATE="../data.json"
NEWFILE="../data.json"

def uPdate(I,IV,O,NewValue):
    with open(FILETOUPADATE, 'r') as ufile:
        data = json.load(ufile)
    if DEBUG: print("Updating :")
    if DEBUG: print("Key :",I,"=",IV)

    if DEBUG: print("Field :",O, "\nwith new value of:\n ",NewValue)
    try:
         #print(data[I])
         #print(f'"{my_str}"')
         print("Before : ",f'<{O}>' ,"IN",f'<{IV}>',"==>",data[IV][O])
         #another way is to print the variable with a wrapper 
         #
         #foo=" within spaces "
         #print(f'{foo!r}')
         #>>>' within spaces 
    except:
        print("Not updated ",data[IV][O],"NOT FOUND")
  
    if type(data[IV][O]) is list:
        print ("Updating list ", data[IV][O])
        data[IV][O].clear()
        data[IV][O].append(NewValue)
    else:
        if type(data[IV][O]) is dict:
            myd={O:NewValue}
            print("Updating Dict ", data[IV][O])
            data[IV][O].update(myd)
        else:
            if type(data[IV][O]) is str:
                data[IV][O]=NewValue
            else:
                print(type(data[IV][O]),"Not type defined will try anyways", data[IV][O])
                data[IV][O]=NewValue
    
    
    print("After :",IV,O,"<==",data[IV][O],"\n")
   
    
    if DEBUG: print("\n")
    with open(NEWFILE,"w") as ofile:
        json.dump(data,ofile)
        

    



with open(INPUTFILE, 'r') as f:
    batchfixes =json.load(f)

 
if type(batchfixes) is list:
     updatesList = batchfixes
     updateDict=None
else:
     if type(batchfixes) is dict:
         updateDict = batchfixes
         updatesList=None

     
 
if updatesList:
     
    for dIdx, xDict in enumerate(updatesList):
        #print("Iteration :",dIdx)
        for uIdx, k in enumerate(xDict.keys()):
            #print("Dict iter =",uIdx)
            #print("Key : ",k, "Value =",xDict[k][:20])
            if uIdx == 0:
                _Index=k
                _IndexValue=xDict[k]
            else:
                _Obj=k
                _ObjNewValue=xDict[k]
                #if DEBUG: _ObjNewValue=xDict[k][:20]
            
        uPdate(_Index,_IndexValue,_Obj,_ObjNewValue)
if updateDict:
    print(f'batchfixes is {type(batchfixes)}')
    for i in updateDict:
        _Index=i
        print("Index =",_Index)
        for _key,_val in updateDict[_Index].items():
            print("K/_Obj = ",_key,"\nVal/_ObjNewValue = ",_val)
            _Obj=_key
            _ObjNewValue=_val
            print("-.-.-.-.-.-.-")
            uPdate("Dict Index",_Index,_Obj,_ObjNewValue)