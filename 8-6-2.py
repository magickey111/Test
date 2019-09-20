
numlist = []
while True:
    inp =input('Enter a number: ')
    if inp == 'done':break
    else:
        value = float(inp)
        numlist.append(value)

print ('Maximum:', max(numlist))
print ('Minimum:', min(numlist))
