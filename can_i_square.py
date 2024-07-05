import math
for i in range(int(input())):
    a = int(input())
    lst = list(map(int,input().split()))
    suma = sum(lst)
    sqrt_n = int(math.sqrt(suma))
    if sqrt_n * sqrt_n == suma:
        print("YES")
    else:
        print("NO")