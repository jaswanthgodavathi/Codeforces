for i in range(int(input())):
    l = list(map(int, input().split()))
    
    if l[0] == l[1] and l[0] == l[2]:
        print("YES")
        print(*l)
    else:
        if l.count(max(l)) == 2:
            print("YES")
            x = list(set(l))
            print(1, *x)
        else:
            print("NO")
