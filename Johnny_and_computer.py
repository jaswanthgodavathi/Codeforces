for i in range(int(input())):
    a,b = map(int,input().split())
    if a == b:
        print("0")
    else:
        if (a < b):
            a, b = b, a
        ans = 0
        while a > b:
            if a//8 >= b and  a % 8 == 0:
                ans += 1 
                a = a//8
            elif a//4 >=b and a%4 == 0:
                ans +=1 
                a = a//4
            elif a//2 >=b and a%2 == 0:
                ans += 1 
                a = a//2
            else:
                break
        if a == b:
            print(ans)
        else:
            print("-1")