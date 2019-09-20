hours=input('Enter Hours: ')
rate=input('Enter Rate: ')
fh=float(hours)
fr=float(rate)
P=fh*fr
if fh <= 40:
    print('Pay: ',P)
if fh > 40:
    print('Pay: ',((fh-40)*fr*1.5+40*fr))
