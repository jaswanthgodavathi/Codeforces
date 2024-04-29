for i in range(int(input())):
    a = int(input())
    b = input()
    c = input()
    flag = 0
    for i in range(len(b)):
        if (b[i] == 'R' and c[i] != 'R') or (b[i] != 'R' and c[i] == 'R'):
            print("NO")
            flag = 1
            break
    if flag == 0:
        print("YES")
