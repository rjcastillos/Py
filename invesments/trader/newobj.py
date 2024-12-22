with open ('template.json','r') as t:
        template = t.read()
print ("TEMPLATE ",template)


TMP=template.replace('NEW','NVDA')

with open('.new_tmp.json','w') as o:
    o.write(TMP)
    
print("TMP temporary",TMP)

import json
with open ('data.json','r') as f:
  Asset = json.load(f)

with open ('.new_tmp.json','r') as t:
	NEW = json.load(t)
 

#print(type(Asset))
#print(type(NEW))
Asset.update(NEW)
fData=json.dumps(Asset,indent=4)


print(fData)

with open ("data.json","w") as o:
    json.dump(Asset,o)