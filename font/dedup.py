from sys import argv, exit

if len(argv) != 2:
    print '[*] Usage: python', argv[0], '<dump>'
    exit()

dump = argv[1]

fp = open(dump, 'rb')

list = []

while True:
    buf = fp.read(2)
    if len(buf) != 2: break
    list.append(buf)

fp.close()

new = dump.split('.')[0] + '.dedup'

fp = open(new, 'wb')

set = set(list)

for i in set:
    fp.write(i)

fp.close()

print '[*] working done'