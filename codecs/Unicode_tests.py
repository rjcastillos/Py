#60a876845e9475285df27ecf5c317eea30028bf75b8988c56b645e9475285e765728767b5f55540e94fe63a560a87684624b673a548c75358111003a002000680074007400700073003a002f002f0061006b0061002e006d0073002f007a00630063006e003f0073003d003800260061003d00260069003d

#https://dencode.com/en/string/hex
#https://unicodelookup.com/#0x60a8/1
#http://xahlee.info/comp/unicode_index.html
#http//bit.ly/unipain

#text is the str type
text='60a876845e9475285df27ecf5c317eea30028bf75b8988c56b645e9475285e765728767b5f55540e94fe63a560a87684624b673a548c75358111003a002000680074007400700073003a002f002f0061006b0061002e006d0073002f007a00630063006e003f0073003d003800260061003d00260069003d'
#textB is the byte type
textB=b'60a876845e9475285df27ecf5c317eea30028bf75b8988c56b645e9475285e765728767b5f55540e94fe63a560a87684624b673a548c75358111003a002000680074007400700073003a002f002f0061006b0061002e006d0073002f007a00630063006e003f0073003d003800260061003d00260069003d'
n=4
[text[i:i+n] for i in range(0, len(text), n)]
unicharstr=[]
unicharstr=[text[i:i+n] for i in range(0, len(text), n)]
unicharByte=[]
unicharByte=[textB[i:i+n] for i in range(0, len(textB), n)]

print('\u60a8')
_you=u'\u60a8'
_youB=b'60a8'
_youG='您'

print ('\u5e76')
_andB=b'5e76'
_and=u'\u5e76'
_andG='并'
_mystrout=u''
for i in unicharstr:
    print("\\u",(i),sep="",end="")
for i in unicharstr:
    _mystrout=_mystrout+"\u"+(i)
print(_mystrout)

_s=''
for i in unicharstr:
    _s=_s+chr(int((i),16))
