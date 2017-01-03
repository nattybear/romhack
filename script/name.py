from sys import argv, exit
from binascii import hexlify, unhexlify
from sqlite3 import connect

if len(argv) != 2:
  print 'Usage:', 'name.py', '<dump>'
  exit()

con = connect('test.db')
cur = con.cursor()

new = 'result.txt'
fp1 = open(new, 'wb')

def convert(hex):
  cur.execute('select hex from japan where id=?', (hex,))
  ret = cur.fetchone()[0]
  ret = unhexlify(ret)
  return ret

offset = 0x3598
fp = open(argv[1], 'rb')
fp.seek(offset)
fp1.write(hex(fp.tell()) + ' ')

while True:
  buf = fp.read(2)
  if len(buf) == 0: break
  if buf != b'\xff\xff':
    buf = hexlify(buf)
    try:
      fp1.write(convert(buf))
    except TypeError:
      pass
  else:
    fp1.write(b'\x0d\x0a')
    fp1.write(hex(fp.tell()) + ' ')
