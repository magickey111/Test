import re


count=0
s=0

fname = input('Enter file: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened: ', fname)
    exit()


for line in fhand:
    line = line.rstrip()
    x= re.findall('^New Revision: ([0-9.]+)', line)
    if x !=[]:
        for val in x:
            count+=1
            s=s+float(val)

print(int(s/count))
