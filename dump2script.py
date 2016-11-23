from sys import argv, exit
from struct import pack

if len(argv) != 3:
    print '[*] Usage: python dump2script.py <dump> <csv>'
    exit()
    
dump = argv[1]
csv = argv[2]

csv_fp = open(csv, 'rb')
csv_buf = csv_fp.read()
csv_fp.close()

csv_list = csv_buf.split(b'\x0d\x0a')
csv_dic = {}

for a, b in enumerate(csv_list):
    csv_dic[a] = b

dump_fp = open(dump, 'rb')

new = dump.split('.')[0] + '.txt'
new_fp = open(new, 'wb')

while True:
    try:
        dump_buf = dump_fp.read(2)
        num = unpack('H', dump_buf)[0]
        if num in csv_dic.keys():
            new_fp.write(dump_buf)
    except:
        break
        
new_fp.close()

print '[*]', new, 'saved'