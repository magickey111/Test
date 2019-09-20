def computergrade(score):
    if score>=0.9:
        G='A'
    elif score>=0.8:
        G='B'
    elif score>=0.7:
        G='C'
    elif score>=0.6:
        G='D'
    else:
        G='F'
    return G10
    

score=input('Enter score: ')
try:
    fs=float(score)
except:
    print('Bad score')
    quit()

T=computergrade(fs)
print(T)
