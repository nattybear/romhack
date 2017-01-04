from sys import argv, exit
from StringIO import StringIO

if len(argv) != 4:
  print 'Usage:', 'name.py', '<rom>', '<offset>', '<name>'
  exit()

rom = argv[1]
offset = argv[2]
name = argv[3]
new = 'out_' + rom

fp1 = open(rom, 'rb')
fp2 = open(offset, 'rb')
fp3 = open(name, 'rb')

buf1 = fp1.read()
buf2 = fp2.read()
buf3 = fp3.read()

fp4 = StringIO(buf1)
fp5 = open(new, 'wb')

list2 = buf2.split(b'\x0d\x0a')
list3 = buf3.split(b'\x0d\x0a')

list22 = [int(i, 16) for i in list2]
list222 = [i + 0x3b0000 for i in list22]

size2 = len(list2)
size3 = len(list3)

if size2 != size3: exit()

for i in range(size2):
  fp4.seek(list222[i])
  fp4.write(list3[i])

fp4.seek(0)
buf4 = fp4.read()

fp5.write(buf4)

print '[*]', new, 'saved'
