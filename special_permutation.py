for i in range(int(input())):
    n = int(input())
    v = list(range(n, 0, -1))
    
    for i in range(n):
        if v[i] == i + 1 and i + 1 < n:
            v[i], v[i + 1] = v[i + 1], v[i]
    
    for i in range(n):
        print(v[i], end=" ")
    print()
