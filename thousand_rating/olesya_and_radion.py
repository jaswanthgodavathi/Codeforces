while True:
    try:
        n, t = map(int, input().split())
        if n == 1 and t == 10:
            print("-1")
        elif n >= 2 and t == 10:
            print("1" * (n - 1) + "0")
        else:
            print(str(t) * n)
    except EOFError:
        break
