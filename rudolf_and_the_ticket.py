for i in range(int(input())):
    count = 0
    a,b, k = map(int,input().split())
    lst1 = list(map(int,input().split()))
    lst2 = list(map(int,input().split()))
    seta = set(lst1)
    setb = set(lst2)
    for i in lst1:
        for j in lst2:
            if i + j <= k:
                count += 1
    print(count)