
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
        for word in words:
            if not word in counts:
                counts[word]=1
            else:
                counts[word]=counts[word]+1

#print(counts)
lst=list()
for key,val in list(counts.items()):
    lst.append((val,key))

lst.sort(reverse=True)

print(lst[0][1],lst[0][0])
