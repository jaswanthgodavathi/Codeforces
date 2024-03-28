for i in range(int(input())):
    lst = list(map(int,input().split()))
    lst.sort(reverse=True)
    if lst[0] + lst[1] >= 10:
        print("YES")
    else:
        print("NO")