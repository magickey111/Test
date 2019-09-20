fh=open('romeo.txt')
L=['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']
for line in fh:
    words=line.split()

    for word in words:
        if not word in L:
            L.append(word)

print(sorted(L))
