sh=input('Enter your houes: ')
sr=input('Enter your rate: ')
fh=float(sh)
fr=float(sr)
if fh<=40:
    print('Pay:',fh*fr)
elif fh>40:
    print('Pay:',((fh-40)*1.5+40)*fr)
