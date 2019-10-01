#!/usr/local/bin/python3.6
#on Mac /usr/local/bin/python3.6
#Or Native /usr/bin/python
##################
#RC Sept 2019
#Program_name: Unicode_test.py
#
#3GPP specs:
# Requirements are based on release V9.1.1 (11) 2010
# https://www.3gpp.org/ftp/Specs/archive/23_series/23.038/
#
#https://dencode.com/en/string/hex
#https://unicodelookup.com/#0x60a8/1
#http://xahlee.info/comp/unicode_index.html
#http://bit.ly/unipain
#Ver. 0.01
#  2019 09
# Ver. 01 2019 09 21
# Inital version receives a Hex literal text as below from the CL and outputs the visual representation in Unicode
# The Hex representation is expected to be from the UCS2 table which is a subset of UTF-16 containing 130.000 codepoints
# out of 1.1M in Unicode , however this program supports all the Unicode codepoints shipped in the used Python distribution
#
#
#Input sample from a PDU
#60a876845e9475285df27ecf5c317eea30028bf75b8988c56b645e9475285e765728767b5f55540e94fe63a560a87684624b673a548c75358111003a002000680074007400700073003a002f002f0061006b0061002e006d0073002f007a00630063006e003f0073003d003800260061003d00260069003d


print('Enter hexadecial Characters:')
text = input()
#text is the str type
#text='60a876845e9475285df27ecf5c317eea30028bf75b8988c56b645e9475285e765728767b5f55540e94fe63a560a87684624b673a548c75358111003a002000680074007400700073003a002f002f0061006b0061002e006d0073002f007a00630063006e003f0073003d003800260061003d00260069003d'
#textB is the byte type
#textB=b'60a876845e9475285df27ecf5c317eea30028bf75b8988c56b645e9475285e765728767b5f55540e94fe63a560a87684624b673a548c75358111003a002000680074007400700073003a002f002f0061006b0061002e006d0073002f007a00630063006e003f0073003d003800260061003d00260069003d'
n=4
#[text[i:i+n] for i in range(0, len(text), n)]
unicharstr=[]
unicharstr=[text[i:i+n] for i in range(0, len(text), n)]
#unicharByte=[]
#unicharByte=[text[i:i+n] for i in range(0, len(text), n)]

#print('\u60a8')
_you=u'\u60a8'
_youB=b'60a8'
_youG='您'

#print ('\u5e76')
_andB=b'5e76'
_and=u'\u5e76'
_andG='并'
_mystrout=u''
#Visually shows the 2bytes parsing
for i in unicharstr:
    print("\\u",(i),sep="",end="")
#
#This way below was a test
# It turns out Py3 handles internally (str) as Unicode and managing escaped backslashes was not that simple
#the way worked better was to convert the Hex value to integer and then use chr()
#for i in unicharstr:
#    _mystrout=_mystrout+"\u"+(i)
#print(_mystrout)

_s=''
for i in unicharstr:
    _s=_s+chr(int((i),16))
print(_s)
