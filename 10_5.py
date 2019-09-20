
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
        atpos=line.find('@')
        sppos=line.find(' ',atpos)
        host=line[atpos+1:sppos]
        word=host
        if not word in counts:
            counts[word]=1
        else:
            counts[word]=counts[word]+1
print(counts)
