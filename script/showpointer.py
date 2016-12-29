from sys import argv
from struct import unpack
from binascii import hexlify

fp = open(argv[1], 'rb')

# get pointer of script pointer array
fp.seek(0x20)
buf = fp.read(2)
ptr = unpack('H', buf)[0]

cnt = 1

fp.seek(ptr)
while True:
  buf = fp.read(2)
  print cnt, hexlify(buf),
  cnt = cnt + 1
  tmp = fp.tell()
  sptr = unpack('H', buf)[0]
  fp.seek(sptr)
  buf = fp.read(2)
  print hexlify(buf)
  if buf != b'\x01\xff':
    if buf != b'\x04\xff': break
  fp.seek(tmp)
