from sys import argv, exit
from struct import pack
from binascii import hexlify

if len(argv) != 2:
    print '[*] Usage: python csv2tbl.py <csv>'
    exit()
    
csv = argv[1]

fp = open(csv, 'rb')
buf = fp.read()
fp.close()

list = buf.split(b'\x0d\x0a')

new = csv.split('.')[0] + '.tbl'
fp = open(new, 'wb')

cnt = 0

for index, char in enumerate(list):
    cnt = index
    index = pack('H', index)
    index = hexlify(index)
    fp.write(index + '=' + char + b'\x0d\x0a')
    
fp.close()

print '[*] Number of tokens : ', cnt