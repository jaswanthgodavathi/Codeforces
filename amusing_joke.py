a = input()
b= input()
c = input()
a = a + b 
a = list(a)
a.sort()
c = list(c)
c.sort()
if a == c:
    print("YES")
else:
    print("NO")