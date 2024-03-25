for i in range(int(input())):
    flag = 0
    a = int(input())
    lst = list(map(int,input().split()))
    lst.sort(reverse=True)
    for i in range(1,len(lst)):
        if lst[i-1] - lst[i] > 1:
            flag = 1
    if flag == 1:
        print("NO")
    else:
        print("YES")