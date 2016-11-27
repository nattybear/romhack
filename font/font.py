from sys import argv, exit
from os import getcwd, mkdir

if len(argv) != 2:
    print '[*] Usage: python font.py <fnt>'
    exit()

fnt = argv[1]

fp1 = open(fnt, 'rb')

dir = getcwd() + '\\fonts\\'

cnt = 0

try:
    mkdir('fonts')
except WindowsError:
    pass

while True:
    name = dir + str(cnt) + '.fnt'
    buf = fp1.read(16)
    if len(buf) != 16: break
    fp2 = open(name, 'wb')
    fp2.write(buf)
    fp2.close()
    cnt = cnt + 1

print '[*] working done'