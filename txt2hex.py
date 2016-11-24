from sys import argv, exit
from struct import pack
from binascii import hexlify

if len(argv) != 3:
    print '[*] Usage: python txt2hex.py <txt> <csv>'
    exit()

txt = argv[1]
csv = argv[2]

fp1 = open(txt, 'rb')

fp2 = open(csv, 'rb')
buf2 = fp2.read()
fp2.close()

list = buf2.split(b'\x0d\x0a')

fp1.seek(3)

while True:
    buf1 = fp1.read(3)
    for a, b in enumerate(list):
        if buf1 == b:
            print hexlify(pack('H', a)),
        else:
            continue
    if len(buf1) == 0:
        break