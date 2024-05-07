t = int(input())
for i in range(t):
    n = int(input())
    base = 1
    result = 0
    for i in range(10, n+1, 10):
        target = i - 1
        result += target // base
        base = base * 10 + 1
    result += n // base
    print(result)
