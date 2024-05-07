for i in range(int(input())):
    a = int(input())
    lst = list(map(int,input().split()))
    count = 0
    for i in range(len(lst)):
        if lst[i]%2 == 0:
            count += 1 
    if count == a:
        print("Yes")
    else:
        print("No")