for i in range(int(input())):
    a = int(input())
    lst = list(map(int,input().split()))
    out = []
    for i in range(len(lst)):
        a,b = input().split()
        b = list(b)
        for j in range(len(b)):
            if b[j] == 'D':
                if lst[i] == 9:
                    lst[i] = 0
                else:
                    lst[i] += 1
            if b[j] == 'U':
                if lst[i] == 0:

                    lst[i] = 9
                else:
                    lst[i] -= 1 
        out.append(lst[i])
    print(' '.join(map(str, out)))
