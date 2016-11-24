from sys import argv, exit
from struct import unpack, error
from binascii import hexlify

if len(argv) != 3:
  print '[*] Usage: python dump2hex.py <dump> <csv>'
  exit()

dump = argv[1]
csv = argv[2]

fp = open(csv, 'rb')
buf = fp.read()
fp.close()
list = buf.split(b'\x0d\x0a')

fp = open(dump, 'rb')
buf1 = ''

while True:
  buf = fp.read(2)
  try:
    num = unpack('H', buf)[0]
    if num == 65535:
      buf1 = buf1 + b'\x0d\x0a'
      continue
  except error:
    break

  try:
    list[num]
    buf1 = buf1 + hexlify(buf) + ' '
  except IndexError:
    buf1 = buf1 + '{' + hexlify(buf) + '}'

fp.close()

new = dump.split('.')[0] + '.hex'
fp = open(new, 'wb')
fp.write(buf1)
fp.close()

print '[*]', new, 'saved'