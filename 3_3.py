sc=input('Enter score: ')
try:
    fs=float(sc)
except:
    print('Bad score')
    quit()

if fs>=0.9:
    print('A')
elif fs>=0.8:
    print('B')
elif fs>=0.7:
    print('C')
elif fs>=0.6:
    print('D')
else:
    print('F')
