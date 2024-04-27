for i in range(int(input())):
    a = input()
    count = 0
    temp = "codeforces"
    for i in range(len(a)):
        if a[i] != temp[i]:
            count += 1
    print(count)