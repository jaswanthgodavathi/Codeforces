t = int(input())
while t > 0:
    a, b, c = map(int, input().split())
    first = abs(a - 1)
    secondA = abs(b - c)
    secondB = abs(c - 1)
    second = secondA + secondB
    if first < second:
        print("1")
    elif second < first:
        print("2")
    else:
        print("3")
    t -= 1
