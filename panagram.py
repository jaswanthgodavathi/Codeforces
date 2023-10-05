a = int(input())
c = input()
c = c.upper()
c = set(c)
if len(c) == 26:
    print("YES")
else:
    print("NO")