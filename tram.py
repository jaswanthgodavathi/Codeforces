c = 0
m = 0
for i in range(int(input())):
    a,b = map(int,input().split())
    c -= a
    c += b 
    if c>m:
        m = c 
print(m)