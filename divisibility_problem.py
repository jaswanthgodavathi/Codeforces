t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    if a % b == 0:
        print(0)
    else:
        div = a // b
        pls = (div + 1) * b
        print(pls - a)
