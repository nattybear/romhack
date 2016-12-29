from sys import argv, exit

if len(argv) != 4:
  print 'Usage:', 'japan2korea.py', '<rom>', '<japan>', '<korea>'
  exit()

rom = argv[1]
japan = argv[2]
korea = argv[3]
new = 'out_' + rom

fp1 = open(rom, 'rb')
fp2 = open(japan, 'rb')
fp3 = open(korea, 'rb')
fp4 = open(new, 'wb')

buf1 = fp1.read()
buf2 = fp2.read()
buf3 = fp3.read()
buf4 = buf1

list2 = buf2.split(b'\x0d\x0a')
list3 = buf3.split(b'\x0d\x0a')

size2 = len(list2)
size3 = len(list3)

if size2 != size3: print '[*] size is not equal'; exit()

for i in range(size2):
  buf4 = buf4.replace(list2[i], list3[i])

fp4.write(buf4)

len1 = len(buf1)
len4 = len(buf4)

print '[*]', new, 'saved'
print '[*] %d bytes changed' % (len4 - len1)
