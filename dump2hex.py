from sys import argv, exit
from binascii import hexlify

def split2(buf):
    tmp = ''
    while buf != '':
        tmp = tmp + buf[:2] + ' '
        buf = buf[2:]
    return tmp

if len(argv) != 2:
    print '[*] Usage: python dump2hex.py <dump>'
    exit()
    
dump = argv[1]

fp1 = open(dump, 'rb')
buf1 = fp1.read()
fp1.close()

list = buf1.split(b'\xff\xff')

new = dump.split('.')[0] + '.hex'
fp2 = open(new, 'wb')

for i in list:
    i = hexlify(i)
    i = split2(i)
    fp2.write(i + b'\x0d\x0a')

fp2.close()

print '[*]', new, 'saved'    