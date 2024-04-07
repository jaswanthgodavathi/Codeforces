for i in range(int(input())):
    x, y, n = map(int, input().split())
    max_multiple = (n - y) // x
    result = x * max_multiple + y
    print(result)


