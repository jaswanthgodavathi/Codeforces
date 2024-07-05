for i in range(int(input())):
    a,b,c = map(int,input().split())
    if a % 2 == 0:
        if b*2 <= c:
            print(a*b)
        else:
            print((a//2)*c)
    else:
        if b*2 <= c:
            print(a*b)
        else:
            print(c*((a-1)//2)+b)
            
