a = input()
upper = 0
lower = 0
for c in a:
    if c.isupper():
        upper += 1 
    if c.islower():
        lower += 1 
if lower >= upper:
    print(a.lower())
else:
    print(a.upper())
