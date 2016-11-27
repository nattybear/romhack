from sys import argv, exit
from os import getcwd

if len(argv) != 3:
    print '[*] Usage: python', argv[0], '<dump>', '<tbl>'
    exit()

dump = argv[1]
tbl = argv[2]

target_dir = getcwd() + '\\fonts\\'

tbl_fp = open(tbl, 'rb')
buf = tbl_fp.read()
tbl_list = buf.split(b'\x0d\x0a')

dump_fp = open(dump, 'rb')
dump_list = []

while True:
    buf = dump_fp.read(2)
    if len(buf) != 2: break
    for a, b in enumerate(tbl_list):
        if buf == tbl_list[a]:
            dump_list.append(a)

new = dump.split('.')[0] + '.fnt'
new_fp = open(new, 'wb')

for i in dump_list:
    fnt = target_dir + str(i) + '.fnt'
    fp = open(fnt, 'rb')
    buf = fp.read()
    fp.close()
    new_fp.write(buf)

print '[*]', new, 'saved'

for i in dump_list:
    print i