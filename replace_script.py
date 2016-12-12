from sys import argv, exit
from struct import pack
from binascii import unhexlify

if len(argv) != 5:
  print 'Usage: python', argv[0], '<before>', '<after>', '<csv>', '<rom>'
  exit()

before = argv[1]
after  = argv[2]
csv    = argv[3]
rom    = argv[4]
new    = 'patched_' + rom

fp1 = open(before, 'rb')
fp2 = open(after, 'rb')
fp3 = open(csv, 'rb')
fp4 = open(rom, 'rb')
fp5 = open(new, 'wb')

buf1 = fp1.read().replace(' ', '')
buf2 = fp2.read()
buf3 = fp3.read()
buf4 = fp4.read()
buf5 = buf4

list3 = buf3.split(b'\x0d\x0a')

for a, b in enumerate(list3):
  i = pack('H', a)
  buf2 = buf2.replace(b, i)

list1 = buf1.split(b'\x0d\x0a')
list2 = buf2.split(b'\x0d\x0a')

cnt = len(list1)

for i in range(cnt):
  list1[i] = unhexlify(list1[i])

for i in range(cnt):
  buf5 = buf5.replace(list1[i], list2[i])

fp5.write(buf5)

print '[*]', new, 'saved'

size1 = len(buf4)
size2 = len(buf5)

print '[*] %s bytes changed' % hex(size2 - size1)