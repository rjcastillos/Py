#!/usr/local/bin/python3.6
#on Mac /usr/local/bin/python3.6
#Or Native /usr/bin/python
##################
#RC Spet 2019
#Program_name: decode_Latin
#Usage : python3 decode_Latin_v01.py
#Takes a Hex literal string from console and decodes it as Latin-1 (ISO 8859 Latin 1)
#
#Content is the message body in an SMS payload , taken from the PDU or with a tcpdump (Sumbit_sm) viewable in wireshark  
#references : http://www.developershome.com/sms/gsmAlphabet.asp
#
####################
#   Import section #
####################
#Import
print('Enter hexadecial Characters:')
line = input()
import codecs
print("Result: \n=======\n",codecs.decode(line,"hex").decode('Latin-1'))
