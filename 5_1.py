T=0
C=0
while True:
  n=input('Enter a number: ')
  if n=='done':
     break
  else:
      try:
         n=float(n)
      except:
         print('Invalid input')
         continue
      T=T+n
      C=C+1
      P=T/C

print(T,C,P)
