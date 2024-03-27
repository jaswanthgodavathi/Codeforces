for i in range(int(input())):
    a = int(input())
    lst = list(map(int,input().split()))
    num = []
    for i in range(len(lst)):
        if lst.count(lst[i]) == 1:
            print(i+1)