import sys
import json
New_Ticker="NEW"
DEBUG=False



if len(sys.argv) > 1:
     New_Ticker=sys.argv[1]
else:
     print("Please indicate a new Ticker to add")
     quit()

print("Creating New json entry for",New_Ticker)

##
#Opening json template file as string
#
with open ('template.json','r') as t:
        template = t.read()


if DEBUG: 
     print ("TEMPLATE ",template)
#
#Replacing place holders from template file with new Ticker
#
TMP=template.replace('NEW',New_Ticker)

with open('.new_tmp.json','w') as o:
    o.write(TMP)
    
if DEBUG :
     print("TMP temporary",TMP)


#
#Opening and loading as Python dict json file to replace
#in further step 
#
with open ('data.json','r') as f:
  Asset = json.load(f)
#
#Opening and loading new Ticker created as string into a Python dict
#
with open ('.new_tmp.json','r') as t:
	NEW = json.load(t)
 

#print(type(Asset))
#print(type(NEW))
#
#Updating Python dict with NEW Ticker's dict entry
#
Asset.update(NEW)
#
#Converting Python dict with all data as string with json format
#
fData=json.dumps(Asset,indent=4)


print("NEW DATA\n",fData)

#
#Replacing current json data file 
#
with open ("data.json","w") as o:
    json.dump(Asset,o)

import os
os.remove(".new_tmp.json")