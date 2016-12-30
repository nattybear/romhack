from sys import argv, exit
from binascii import hexlify

if len(argv) != 2:
  print '[*]', 'duplicate.py', '<txt>'
  exit()

fp = open(argv[1], 'rb')
buf = fp.read()
mylist = buf.split(b'\x0d\x0a')

for a, i in enumerate(mylist):
  num = buf.count(i)
  if num != 1:
    print num, a+1, hexlify(i)

print '[*] scan finish'
