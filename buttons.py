for i in range(int(input())):
    a,b,c = map(int,input().split())
    if a > b:
        print("First")
    elif a < b:
        print("Second")
    elif c%2 != 0:
        print("First")
    else:
        print("Second")