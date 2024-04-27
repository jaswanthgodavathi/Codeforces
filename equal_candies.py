for i in range(int(input())):
    a = int(input())
    lst = list(map(int,input().split()))
    mini = min(lst)
    c = 0
    for i in range(len(lst)):
        c += lst[i] - mini
    print(c)