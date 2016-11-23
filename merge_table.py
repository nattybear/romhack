from sys import argv, exit

if len(argv) != 3:
    print '[*] Usage: python merge_table.py <tbl1> <tbl2>'
    exit()
    
tbl1 = argv[1]
tbl2 = argv[2]

fp1 = open(tbl1, 'rb')
buf1 = fp1.read()
fp1.close()

fp2 = open(tbl2, 'rb')
buf2 = fp2.read()
fp2.close()

new = tbl1.split('.')[0] + '+' + tbl2.split('.')[0] + '.tbl'
fp3 = open(new, 'wb')
fp3.write(buf1 + buf2)
fp3.close()

print '[*] ', new, 'saved'