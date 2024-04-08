for i in range(int(input())):
    lst = list(map(int,input().split()))
    for i in range(len(lst)):
        if lst.count(lst[i]) == 1:
            print(lst[i])