fn=input('Enter a file name: ')
#print(fn)
c=0
value=0
fhand=open(fn)
for line in fhand:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    else:
        line=line.rstrip()
        c=c+1
        index_value=line.find(':')+1
        value=float(line[index_value:])+value
    #print(line)

#print(c)
print("Average spam confidence:",value/c)
