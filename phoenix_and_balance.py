import math
t = int(input().strip())
for case in range(t):
    ans = 0
    sum1 = 0
    sum2 = 0
    n = int(input().strip())
    a = [0] * 10000
    k = 0
    for i in range(1, n + 1):
        a[k] = 2 ** i
        k += 1
    div = n // 2
    sum1 = a[n - 1]
    for i in range(div - 1):
        sum1 += a[i]
    for i in range(div - 1, n - 1):
        sum2 += a[i]
    ans = abs(sum1 - sum2)
    print(ans)
