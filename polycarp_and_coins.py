t = int(input())
for i in range(t):
    n = int(input())
    c1 = n // 3
    c2 = n // 3

    if n % 3 == 1:
        c1 += 1
    elif n % 3 == 2:
        c2 += 1

    print(c1, c2)
