a,b = map(int,input().split())
if a == b:
    print(1)
else:
    count = 0
    while a<=b:
        a = a*3
        b = b*2
        count += 1
    print(count)