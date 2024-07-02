for i in range(int(input())):
    n,k = map(int, input().split())
    lst = list(map(int,input().split()))
    flag = 0
    for i in range(n):
        if lst[i] == k:
            print("YES")
            flag = 1
            break
    if flag == 0:
        print("NO")
        