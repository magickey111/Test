def count(str,let):
    word=str
    c=0
    for letter in word:
        if letter == let:
            c=c+1
    return c

str=input('Enter str: ')
print(str)
let=input('Enter letter: ')
print(let)

T=count(str,let)
print(T)
