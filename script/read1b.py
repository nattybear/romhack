from sys import argv
from struct import unpack, pack
from binascii import hexlify

fp = open(argv[1], 'rb')

while True:
  buf1 = fp.read(1)
  if len(buf1) == 0: break
  buf2 = unpack('B', buf1)[0]

  if buf2 < 0xb0:
    print buf1

  else:
    buf1 = buf1 + fp.read(1)
    print buf1
