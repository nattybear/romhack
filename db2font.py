from sqlite3 import connect
from binascii import unhexlify

con = connect('test.db')
cur = con.cursor()

cur.execute('select * from test')

rows = cur.fetchall()

new = 'fontsrc.txt'
fp = open(new, 'wb')

for i in rows:
  i = i[1]
  i = unhexlify(i)
  if len(i) == 1:
    fp.write(i + ' ')
  else:
    fp.write(i)

print '[*]', new, 'saved'
