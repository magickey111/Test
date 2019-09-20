str = 'X-DSPAM-Confidence:0.8475'
m=str.find(':')
print(m)
host=str[m+1:]
print(host)
n=float(host)
print(n)
