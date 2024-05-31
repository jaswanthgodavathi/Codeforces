t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    maxi = 0
    c = 0
    for num in a:
        if num == 0:
            c += 1
            maxi = max(maxi, c)
        else:
            c = 0
    print(maxi)
