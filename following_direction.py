for i in range(int(input())):
    a = int(input())
    string = input()
    flag = 0
    outx, outy = 0, 0
    for i in range(len(string)):
        if string[i] == 'U':
            outy += 1
        elif string[i] == 'D':
            outy -= 1
        elif string[i] == 'R':
            outx += 1
        elif string[i] == 'L':
            outx -= 1
        if outx == 1 and outy == 1:
            flag = 1
    if flag == 1:
        print("YES")
    else:
        print("NO")