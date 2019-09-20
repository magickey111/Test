fhand=open('mbox-short.txt')
print(fhand)
for k in fhand:
    k=k.rstrip()
    print(k.upper())
