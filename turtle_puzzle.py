for i in range(int(input())):
    a = int(input())
    lst = list(map(int,input().split()))
    sump = 0 
    for i in range(len(lst)):
        if lst[i] < 0:
            sump -= lst[i]
        else:
            sump += lst[i]
    print(sump)