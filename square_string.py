for i in range(int(input())):
    a = input()
    if len(a)%2 == 1:
        print("NO")
    else:
        mid = len(a)//2
        part1 = a[:mid]
        part2 = a[mid:]
        if part1 == part2:
            print("YES")
        else:
            print("NO")
