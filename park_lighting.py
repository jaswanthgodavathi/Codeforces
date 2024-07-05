import math
for i in range(int(input())):
    n,m = map(int,input().split())
    A,B  = float(n), float(m)
    ans = math.ceil((A*B)/2)
    print(int(ans))