a = int(input())
if a == 0:
    print("0")
else:
    count = 0
    while a//10 > 0:
        b = list(str(a) )
        tot = sum(int(x) for x in b)
        a = tot
        count += 1 
    print(count)