from sys import argv, exit
from sqlite3 import connect, IntegrityError
from binascii import unhexlify, hexlify
from struct import unpack, pack

if len(argv) != 2:
  print 'Usage:', 'db2.py', '<txt>'
  exit()

txt = argv[1]
fp = open(txt, 'rb')
buf = fp.read()
mylist = buf.split(b'\x0d\x0a')

con = connect('test.db')
cur = con.cursor()

cur.execute('select * from test')
rows = cur.fetchall()

a = rows[-1][0]
a = unhexlify(a)
a = unpack('H', a)[0]

a = a + 1

for i in mylist:
  i = hexlify(i)
  b = pack('H', a)
  b = hexlify(b)
  t = (b, i)
  try:
    cur.execute('insert into test values(?, ?)', t)
    a = a + 1
  except IntegrityError:
    pass

con.commit()
