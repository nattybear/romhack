from sys import argv, exit

if len(argv) != 4:
    print '[*] Usage: python dump.py <rom> <start> <end>'
    exit()
    
rom = argv[1]
start = int(argv[2], 16)
end = int(argv[3], 16)
size = end - start + 1

fp = open(rom, 'rb')
fp.seek(start)
buf = fp.read(size)
fp.close()

new = hex(start) + '-' + hex(end) + '.dump'

fp = open(new, 'wb')
fp.write(buf)
fp.close()

print '[*] dump size :', size
print '[*]', new, 'saved'