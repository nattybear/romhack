from sys import argv, exit
from binascii import hexlify

if len(argv) != 3:
  print 'Usage:', 'check.py', '<rom>', '<bin>'
  exit()

rom = argv[1]
bin = argv[2]

fp1 = open(rom, 'rb')
fp2 = open(bin, 'rb')

buf1 = fp1.read()
buf2 = fp2.read()

list2 = buf2.split(b'\x0d\x0a')

for a, b in enumerate(list2):
  ret = buf1.find(b)
  if ret == -1:
    b = hexlify(b)
    print a+1, b

print '[*] scan finished'
