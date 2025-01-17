import requests
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0'}
url='https://www.customainze.com/'
r = requests.get(url, headers=headers)
print(r,"E =>",r.encoding)
#quit()
html=r.text
#print(html)
with open('.tmp.html','w') as o:
    o.write(html)