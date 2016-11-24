from sys import argv
from PIL import Image
from struct import unpack
from binascii import hexlify

def parse(buf):
  size = len(buf) / 2
  return unpack('H' * size, buf)

def num2img(num):
  fn = '.\\font\\' + str(num) + '.bmp'
    
  try:
    return Image.open(fn)
  except IOError as e:
    return None

fp = open(argv[1], 'rb')
buf = fp.read()
fp.close()

buf = buf.split(b'\xff\xff')

size = []

for i in buf:
  size.append(len(i))

x_max = max(size) / 2 * 8
y_max = len(buf) * 16

new_im = Image.new('P', (x_max, y_max))

y1 = 0
y2 = 16

for i in buf:

  x1 = 0
  x2 = 8

  for j in parse(i):

    im = num2img(j)

    if im == None:
      continue

    new_im.paste(im, (x1, y1, x2, y2))
    x1 = x2
    x2 = x2 + 8

  y1 = y2
  y2 = y2 + 16

new = argv[1].split('.')[0] + '.bmp'
new_im.save(new)
new_im.show()