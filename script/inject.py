from sys import argv, exit

if len(argv) != 4:
  print 'Usage: ', 'inject.py', '<src>', '<rom>', '<offset>'
  exit()

font = argv[1]
rom = argv[2]
offset = int(argv[3], 16)
new = 'inject_' + rom

fp1 = open(font, 'rb')
fp2 = open(rom, 'rb')
fp3 = open(new, 'wb')

buf1 = fp1.read()
buf2 = fp2.read()

fontsize = len(buf1)
end = offset + fontsize

buf3 = buf2[:offset] + buf1 + buf2[end:]

fp3.write(buf3)

print '[*]', new, 'saved'
