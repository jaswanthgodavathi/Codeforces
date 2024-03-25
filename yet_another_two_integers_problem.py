for i in range(int(input())):
    a,b = map(int,input().split())
    if a == b:
        print(0)
    else:
        if a > b:
            if (a-b)%10 == 0:
                print((a-b)//10)
            else:
                print(((a-b)//10 )+ 1)
        elif b > a:
            if (b-a)%10 == 0:
                print((b-a)//10)
            else:
                print(((b-a)//10 )+ 1)
