for i in range(int(input())):
    a = int(input())
    str = input()
    lst = []
    count = 0
    for i in range(len(str)):
        if str[i] not in lst:
            count += 2
            lst.append(str[i])
        else:
            count += 1
    print(count)