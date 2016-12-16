from sys import argv, exit
from binascii import unhexlify

if len(argv) != 4:
  print 'Usage: python', argv[0], '<before>', '<after>', '<rom>'
  exit()

before = argv[1]
after = argv[2]
rom = argv[3]
new = '_' + rom

before1 = unhexlify(before)
after1 = unhexlify(after)

fp1 = open(rom, 'rb')
fp2 = open(new, 'wb')

buf1 = fp1.read()
buf2 = buf1.replace(before1, after1)

fp2.write(buf2)

print '[*]', before, '->', after
print '[*]', new, 'saved'
