from sys import argv, exit

if len(argv) != 3:
  print 'Usage:', 'findoffset.py', '<txt>', '<rom>'
  exit()

txt = argv[1]
rom = argv[2]

fp1 = open(txt, 'rb')
fp2 = open(rom, 'rb')

buf1 = fp1.read()
buf2 = fp2.read()

offset = buf2.find(buf1)

if offset == -1:
  print '[*] There is no such binary'

else:
  print '[*] offset:', hex(offset)
