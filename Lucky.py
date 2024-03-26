for i in range(int(input())):
    a = input()
    first = list(a[:3])
    last = list(a[-3:])
    sumf = 0
    suml = 0
    for i in range(3):
        sumf += ord(first[i])
        suml += ord(last[i])
    if sumf == suml:
        print("YES")
    else:
        print("NO")