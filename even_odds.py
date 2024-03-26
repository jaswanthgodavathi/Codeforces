a,b = map(int,input().split())
if a%2 == 0:
    diff = a//2
    if b>diff:
        print(2*(b-diff))
    else:
        print(1+2*(b-1))
else:
    diff = a//2 + 1
    if b > diff:
        print(2*(b-diff))
    else:
        print(1+2*(b+1))
        

