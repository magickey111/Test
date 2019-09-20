largest=None
smallest=None
while True:
  n=input('Enter a number: ')
  if n=='done':
     print(largest,smallest)
  else:
      try:
         n=float(n)
      except:
         print('Invalid input')
         continue
      if largest is None or largest < n:
         largest=n
      if smallest is None or smallest > n:
         smallest=n
      print(largest,smallest)
