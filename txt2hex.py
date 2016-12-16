from sys import argv, exit
from struct import pack
from binascii import hexlify

if len(argv) != 3:
  print 'Usage: python', argv[0], '<txt>', '<csv>'
  exit()

txt = argv[1]
csv = argv[2]
new = 'hex_' + txt

fp1 = open(txt, 'rb')
fp2 = open(csv, 'rb')
fp3 = open(new, 'wb')

buf1 = fp1.read()
buf1 = buf1[3:]
buf2 = fp2.read()
buf2 = buf2[3:]

list2 = buf2.split(b'\x0d\x0a')

for a, b in enumerate(list2):
  a = pack('H', a)
  a = hexlify(a)
  buf1 = buf1.replace(b, a)

fp3.write(buf1)

print '[*]', new, 'saved'
