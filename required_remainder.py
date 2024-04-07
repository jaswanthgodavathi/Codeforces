for i in range(int(input())):
    x,y,n = map(int,input().split())
    for i in range(n,-1,-1):
        if i%x == y:
            print(i)
            break

