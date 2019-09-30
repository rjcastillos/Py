#!/usr/local/bin/python3.6
#on Mac /usr/local/bin/python3.6
#Or Native /usr/bin/python
##################
#RC Sett 2019
#Program_name: decode
#Usage : python3 decode_Latin_v01.py
#Takes a Hex literal string from console and decodes it as GSM 03.38
#
#Content is the message body in an SMS payload , taken from the PDU or with a tcpdump (Sumbit_sm) viewable in wireshark  
#
#references : http://www.developershome.com/sms/gsmAlphabet.asp
#
####################
#   Import section #
####################
#Import
print('Enter hexadecial Characters:')
line = input()
n=2
hex_pair=[line[i:i+n] for i in range(0, len(line), n)]
def gsm7bitdecode(text):
    gsm = (u"@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞ\x1bÆæßÉ !\"#¤%&'()*+,-./0123456789:;<=>"
           u"?¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ`¿abcdefghijklmnopqrstuvwxyzäöñüà")
    ext = (u"````````````````````^```````````````````{}`````\\````````````[~]`"
           u"|````````````````````````````````````€``````````````````````````")

    print ("Converting", text)
    text = ''.join(["{0:08b}".format(int(text[i:i+2], 16)) for i in range(0, len(text), 2)][::-1])
    print ("binary 8 bits" ,text)
    text = [(int(text[::-1][i:i+7][::-1], 2)) for i in range(0, len(text), 7)]
    print (text)
    text = text[:len(text)-1] if text[-1] == 0 else text
    print ("Decimal value",text)
    text =iter(text)


    result = []
    for i in text:
        if i == 27:
            i = next(text)
            result.append(ext[i])
        else:
            result.append(gsm[i])

    return "".join(result).rstrip()
#print(gsm7bitdecode('5261'))
messa=[]
for i in hex_pair:
    print(gsm7bitdecode(i))
    messa.append(str(gsm7bitdecode(i)))
print("Body =>",''.join(messa))
