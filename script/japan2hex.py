from sys import argv, exit
from StringIO import StringIO
from sqlite3 import connect
from struct import unpack
from binascii import unhexlify, hexlify

if len(argv) != 2:
  print 'Usage:', 'japan2hex.py', '<japan>'
  exit()

japan = argv[1]
new = 'japan.hex'

fp1 = open(japan, 'rb')
fp2 = open(new, 'wb')

buf1 = fp1.read().replace(b'\xef\xbb\xbf', '')

mylist1 = buf1.split(b'\x0d\x0a')
mylist2 = []

def db(char):
  char = hexlify(char)
  con = connect('test.db')
  cur = con.cursor()
  cur.execute('select id from japan where hex=?', (char,))
  ret = cur.fetchone()[0]
  ret = unhexlify(ret)
  return ret

def readline(line):
  ret = ''
  fp = StringIO(line)
  while True:
    buf = fp.read(1)
    if len(buf) == 0: break
    
    buf2 = unpack('B', buf)[0]

    if buf2 == 0x20:
      ret = ret + db(buf)

    elif buf2 == 0xd0:
      buf = buf + fp.read(1)
      ret = ret + db(buf)

    else:
      buf = buf + fp.read(2)
      ret = ret + db(buf)

  return ret

for i in mylist1:
  mylist2.append(readline(i))

buf2 = b'\x0d\x0a'.join(mylist2)
fp2.write(buf2)

print '[*]', new, 'saved'
