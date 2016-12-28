from sys import argv, exit
from sqlite3 import connect
from struct import pack
from binascii import hexlify

if len(argv) != 2:
  print 'Usage:', 'db.py', '<txt>'
  exit()

txt = argv[1]
fp = open(txt, 'rb')
buf = fp.read()
mylist = buf.split(b'\x0d\x0a')

con = connect('test.db')
cur = con.cursor()

for a, b in enumerate(mylist):
  a = pack('H', a)
  a = hexlify(a)
  b = hexlify(b)
  t = (a, b)
  cur.execute('insert into test values (?, ?)', t)

con.commit()
