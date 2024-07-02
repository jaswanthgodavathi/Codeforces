for i in range(int(input())):
    a = int(input())
    s = input()
    lt = 0
    rt = len(s)
    for x in s:
        if x == 'B':
            break
        lt += 1
    for x in s[::-1]:
        if x == 'B':
            break
        rt -= 1
    print(rt - lt)
