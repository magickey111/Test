import string
fname=input('Enter file name: ')
fh=open(fname)
counts=dict()

for line in fh:
    line=line.translate(str.maketrans(' ',' ',string.punctuation))
    line=line.translate(str.maketrans(' ',' ',string.digits))
    line=line.lower()
    line=line.strip()
    words=line.split()
    for word in words:
        for letter in word:
            counts[letter]=counts.get(letter,0)+1
        

print(sorted([(v,k) for k,v in counts.items()]))