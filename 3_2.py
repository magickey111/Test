sh=input('Enter Hours: ')
try :
    fh=float(sh)
except:
    print('Error, please enter numeric input')
    quit()
sr=input('Enter Rate: ')
try:
    fr=float(sr)
except:
    print('Error, please enter numeric input')
    quit()

P=fh*fr
if fh<=40:
    print('Pay:',P)
else:
    print('Pay:',((fh-40)*1.5+40)*fr)
