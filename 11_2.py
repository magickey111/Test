
fname=input('Enter a file name: ')
counts=dict()

try:
    fh=open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

for line in fh:
    line=line.strip()
    if line.startswith('From '):
        words=line.split()
        col_pos=words[5].find(':')
        word=words[5][:col_pos]
        if not word in counts:
            counts[word]=1
        else:
            counts[word]=counts[word]+1

#print(counts)
lst=list()
for key,val in list(counts.items()):
    lst.append((key,val))

lst.sort()

for key,val in lst:
    print(key,val)
