for i in range(int(input())):
    a = int(input())
    lst = list(map(int,input().split()))
    suma = 0
    odda = 0
    for i in range(len(lst)):
        if lst[i]%2 == 0:
            suma += lst[i]
        else:
            odda += lst[i]
    if suma > odda:
        print("YES")
    else:
        print("NO")