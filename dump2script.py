from sys import argv, exit
from struct import pack

if len(argv) != 3:
    print '[*] Usage: python dump2script.py <dump> <csv>'
    exit()
    
dump = argv[1]
csv = argv[2]

fp1 = open(dump, 'rb')
buf1 = fp1.read()
fp1.close()

fp2 = open(csv, 'rb')
buf2 = fp2.read()
fp2.close()

list = buf2.split(b'\x0d\x0a')

for index, char in enumerate(list):
    index = pack('H', index)
    buf1 = buf1.replace(index, char)
    
buf1 = buf1.replace(b'\xff\xff', b'\x0d\x0a')
buf1 = b'\xef\xbb\xbf' + buf1

new = dump.split('.')[0] + '.txt'
fp = open(new, 'wb')
fp.write(buf1)
fp.close()

print '[*]', new, 'saved'