def computerpay(hours,rate):
    if hours<=40:
        P=hours*rate
    else:
        P=((hours-40)*1.5+40)*rate
    return P

hours=input('Enter Hours: ')
try :
    fh=float(hours)
except:
    print('Error, please enter numeric input')
    quit()
rate=input('Enter Rate: ')
try:
    fr=float(rate)
except:
    print('Error, please enter numeric input')
    quit()

XP=computerpay(fh,fr)
print('Pay:',XP)
