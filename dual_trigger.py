a = int(input())
for i in range(a):
    t = int(input())
    count = 0
    str = input()
    for i in range(len(str)):
        if str[i] == '1':
            count += 1
    if count % 2 == 0:
        print("YES")
    else:
        print("NO")
