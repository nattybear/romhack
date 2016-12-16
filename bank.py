from sys import argv, exit

if len(argv) != 2:
  print 'Usage: python', argv[0], '<rom>'
  exit()

rom = argv[1]
fp1 = open(rom, 'rb')

cnt = 0

while True:
  buf = fp1.read(0x10000)
  if len(buf) != 0x10000: break
  name = str(cnt) + '.bank'
  fp2 = open(name, 'wb')
  fp2.write(buf)
  cnt = cnt + 1

print '[*] Number of banks :', str(cnt)
