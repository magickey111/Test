import re
hand = open('mbox.txt')
num=0
inp=input('Enter a regular expression: ')
reg=str(inp)

for line in hand:
    line = line.rstrip()
    if re.findall(reg, line) !=[]:
        num+=1
    

print('mbox.txt','had',num,'lines that matched',reg)

    