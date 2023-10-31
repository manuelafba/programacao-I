import re

msg = 'aaaaaa'

saida = len(msg) % 2 == 0 and\
    re.compile(r'[a]+')

if saida:
    print("ok")
else:
    print("fail")