from sys import argv, exit
from binascii import hexlify, unhexlify
from sqlite3 import connect

if len(argv) != 2:
  print 'Usage:', 'hexwithchar.py', '<bin>'
  exit()

bin = argv[1]
new = 'out.txt'

fp1 = open(bin, 'rb')
fp2 = open(new, 'wb')

list1 = []
list2 = []

while True:
  buf1 = fp1.read(2)
  if len(buf1) == 0: break
  buf1 = hexlify(buf1)
  list1.append(buf1)

con = connect('test.db')
cur = con.cursor()

for i in list1:
  cur.execute('select hex from japan where id=?', (i,))
  try:
    ret = cur.fetchone()[0]
    ret = unhexlify(ret)
  except:
    ret = b'\x20'

  list2.append(ret)

for i in list1:
  fp2.write(i + '\t')

fp2.write(b'\x0d\x0a')

for i in list2:
  fp2.write(i + '\t')

print '[*]', new, 'saved'
