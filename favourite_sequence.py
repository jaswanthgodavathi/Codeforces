for i in range(int(input())):
    a = int(input())
    lst = list(map(int,input().split()))
    out = []
    if len(lst)%2 == 0:
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]
        right.reverse()
        for i in range(len(left)):
            out.append(left[i])
            out.append(right[i])
    if len(lst)%2 == 1:
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]
        right.reverse()
        middle = lst[mid]
        for i in range(len(left)):
            out.append(left[i])
            out.append(right[i])
        out.append(middle)
    for i in range(len(out)):
        print(out[i], end = " ")