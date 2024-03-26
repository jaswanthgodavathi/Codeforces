n, m = map(int, input().split())
a = list(map(int, input().split()))
b = [int(input()) for _ in range(m)]

t = 1
sum_val = 0

for x in b:
    while sum_val + a[t - 1] < x:
        sum_val += a[t - 1]
        t += 1
    print(sum_val)
    print(t, x - sum_val)