from sys import argv, exit
from struct import unpack

if len(argv) != 2:
    print '[*] Usage: python', argv[0], '<dump>'
    exit()

dump = argv[1]
fp1 = open(argv[1], 'rb')

new = argv[1].split('.')[0] + '.rmob'
fp2 = open(new, 'wb')

while True:
    buf = fp1.read(1)
    if len(buf) == 0: break
    num = unpack('B', buf)[0]
    if num >= 0xa0:
        fp2.write(buf)

print '[*] working done'