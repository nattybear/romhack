from sys import argv, exit
from binascii import hexlify

if len(argv) != 2:
  print 'Usage:', argv[0], '<bin>'
  exit()

fp = open(argv[1], 'rb')

while True:
  buf = fp.read(1)
  if len(buf) == 0: break
  buf = hexlify(buf)
  print buf,
