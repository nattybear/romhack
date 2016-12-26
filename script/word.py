from sys import argv, exit
from binascii import hexlify
from pickle import load
from StringIO import StringIO

if len(argv) != 3:
    print 'Usage: word.py', '<input>', '<dict>'
    exit()

a = argv[1]
b = argv[2]
b = open(b, 'rb')

mydict = load(b)

a = StringIO(a)

while True:
    buf = a.read(2)
    if len(buf) != 2: break
    try:
        print buf, mydict[buf]
    except KeyError as e:
        print ''
