Asset=	{'NEW':	{'name':'Realty Income Corporation (O)',
		'Ticker':'NEW',
		'Div':0.00,
		'Price':0.00,
		'Periodicity':'Q',
		'Qty':0,
		'NextExDate':'20250102',
		'Position':[
				{'On':'True',
				 'Strategy':'SniperOne',
				 'Qty':0,
				 'Direction':'Long',
				 'DateIn':'',
				 'PriceIn':00.00,
				 'DateOut':'',
				 'PriceOut':'',
				 'DateOut':''
				}
			    ]
					 
		}
	}
print(Asset)
print(Asset['o']['Position'][0]['Strategy'])
import json 
with open ("Asset.json","w") as o:
    json.dump(Asset,o)