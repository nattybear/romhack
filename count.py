from sys import argv, exit

if len(argv) != 2:
    print '[*] Usage: python count.py <txt>'
    exit()

txt = argv[1]

fp = open(txt, 'rb')
buf = fp.read()
fp.close()

buf = buf.replace(b'\x20', '')
list = []

while True:
    list.append(buf[:2])
    buf = buf[2:]
    if buf == '':
        break

set = set(list)

cnt = len(set)

print '[*] Number of char : %d' % cnt

for i in set:
    print i