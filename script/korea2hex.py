from sys import argv, exit
from StringIO import StringIO
from sqlite3 import connect
from binascii import unhexlify, hexlify
from struct import unpack

def char2num(char):
    con = connect('test.db')
    cur = con.cursor()
    cur.execute('select id from test where hex=?', (char,))
    ret = cur.fetchone()
    con.close()
    ret = unhexlify(ret[0])
    return ret

def read1byte(line):
    buf = ''
    fp = StringIO(line)
    while True:
        buf1 = fp.read(1)
        if len(buf1) == 0: break
        buf2 = unpack('B', buf1)[0]

        if buf2 < 0xa1:
            buf1 = hexlify(buf1)
            ret = char2num(buf1)
            buf = buf + ret

        else:
            buf1 = buf1 + fp.read(1)
            buf1 = hexlify(buf1)
            ret = char2num(buf1)
            buf = buf + ret

    return buf

if len(argv) != 2:
  print 'Usage:', 'korea2hex.py', '<txt>'
  exit()

fp = open(argv[1], 'rb')
fp1 = open('output.bin', 'wb')

buf = fp.read()
mylist = buf.split(b'\x0d\x0a')
mylist2 = []

for i in mylist:
    mylist2.append(read1byte(i))

buf1 = b'\x0d\x0a'.join(mylist2)

fp1.write(buf1)

print '[*]', 'output.bin', 'saved'
