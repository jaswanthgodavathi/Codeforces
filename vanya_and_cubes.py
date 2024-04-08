n = int(input())
cnt = 0
i = 1
m = 1

while m <= n:
    m = ((i*i) + i) // 2

    if m > n:
        break

    n -= m
    cnt += 1
    i += 1

print(cnt)
