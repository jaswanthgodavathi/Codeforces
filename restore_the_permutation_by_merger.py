for i in range(int(input())):
    a = int(input())
    lst = list(map(int, input().split()))
    out = []
    for i in lst:
        if i not in out:
            out.append(i)
    for i in range(len(out)):
        print(out[i], end = " ")
