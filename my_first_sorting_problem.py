for i in range(int(input())):
    a,b = map(int,input().split())
    if a > b:
        print(b, a)
    else:
        print(a, b)
