
import string

fname=input('Enter a file name: ')
counts=dict()

try:
    fh=open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

for line in fh:
    line=line.strip()
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.lower()
    words=line.split()
    for word in words:
        for letter in word:
            if not letter in counts:
                counts[letter]=1
            else:
                counts[letter]+=1

#print(counts)
lst=list()
for key,val in list(counts.items()):
    lst.append((key,val))

lst.sort(reverse=True)

for key,val in lst:
    print(key,val)
