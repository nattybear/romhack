from sys import argv, exit
from struct import unpack, pack

if len(argv) != 2:
    print '[*] Usage: python remove_cc.py <dump>'
    exit()
    
dump = argv[1]
fp = open(dump, 'rb')

new = dump.split('.')[0] + '.nocc'
fp1 = open(new, 'wb')

while True:
    try:
        buf = fp.read(2)
        buf = unpack('H', buf)[0]
    
        if buf == 0xff01: # face(num)
            fp.read(2)
            continue
        elif buf == 0xff03: # unknown
            continue
        elif buf == 0xff05: # music(num)
            fp.read(2)
            continue
        elif buf == 0xff07: # display?
            continue
        elif buf == 0xff08: # screen(cc)
            continue
        elif buf == 0xff09: # background(num)
            fp.read(2)
            continue
        elif buf == 0xff0c: # unknown(a)
            fp.read(2)
            continue
        elif buf == 0xff0e: # wait(time)
            fp.read(2)
            continue
        elif buf == 0xff11: # end(a)
            fp.read(2)
            continue
        elif buf == 0xffff: # enter
            buf = pack('H', buf)
            fp1.write(buf)
        elif buf > 0xff00: # etc
            continue
        else:
            buf = pack('H', buf)
            fp1.write(buf)
    except:
        break
        
fp.close()
fp1.close()

print '[*]', new, 'saved'