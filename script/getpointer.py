from sys import argv, exit
from struct import pack

if len(argv) != 4:
  print 'Usage:', argv[0], '<dump>', '<start>', '<end>'
  exit()

dump = argv[1]
start = int(argv[2], 16)
end = int(argv[3], 16)
new = 'pointer.bin'

list1 = []

fp1 = open(dump, 'rb')
fp2 = open(new, 'wb')

list1.append(start)

fp1.seek(start)

while True:
  buf = fp1.read(2)
  if fp1.tell() > end: break
  if buf == b'\xfe\xff':
    list1.append(fp1.tell())

for i in list1:
  i = pack('H', i)
  fp2.write(i)

print '[*]', new, 'saved'
