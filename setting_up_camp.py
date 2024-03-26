for i in range(int(input())):
    sum = 0
    a,b,c = map(int,input().split())
    sum += a
    if b % 3 == 0:
        sum += (b)//3
        if c%3 == 0:
            sum += c//3
        else:
            sum += c//3 + 1
    else:
        if (b%3) + c >=3:
            if ((b%3) + c) % 3 == 0:
                sum += ((b) + c) // 3
            else:
                sum += ((b) + c) // 3 + 1
        else:
            sum = -1 
    print(sum)